#include <stdlib.h>
#include <stdio.h>

#include "delay.h"
#include "sys.h"

//乐曲数量(最大10首)
int musicNum;
//音阶
int *notes[11];
//持续时间(s)
double *times[11];

//音阶对应周期(us)
const int ct[128]={57736,54466,51440,48543,45829,43252,40816,38520,36363,34317,32404,30581,28868,27247,25706,24271,22904,21626,20408,19260,18181,17158,16196,15290,14430,13620,12856,12135,11454,10810,10204,9632,9090,8580,8098,7644,7215,6810,6428,6067,5726,5405,5102,4815,4545,4290,4049,3822,3607,3405,3214,3033,2863,2702,2551,2407,2272,2145,2024,1911,1803,1702,1607,1516,1431,1351,1275,1203,1136,1072,1012,955,901,851,803,758,715,675,637,601,568,536,506,477,450,425,401,379,357,337,318,300,284,268,253,238,225,212,200,189,178,168,159,150,142,134,126,119,112,106,100,94,89,84,79,75,71,67,63,59,56,53,50,47,44,42,39,37,};

extern void beepOn(void);
extern void beepOff(void);
extern void beepInit(void);

/*各个函数初始化*/
void init(){
	sys_stm32_clock_init(336, 8, 2, 7);
  	delay_init(168);
	beepInit();
}

/*播放音符持续一段时间
  note: 	音阶号[0,127]
  timeUs: 	持续时间(us)
*/
void playNote(int note,int timeUs){
	for(int d=0;d<timeUs;d+=ct[note]){
		beepOn();
		delay_us(ct[note]/2);
		beepOff();
		delay_us(ct[note]/2);
	}
}

/*播放曲目
  note:	音符数组
  time: 持续时间数组
*/
void play(int *note,double *time){
	for(int i=0;i<note[0];++i)
		playNote(note[i],time[i]);
}

/*从文件加载曲目
  曲目文件夹res\存放*.txt
  从1.txt开始扫描
*/
void load(){
	FILE *musicFile;
	char fileName[100];
	for(int i=1;;++i){
		sprintf(fileName,"res/%d.txt",i);
		if(NULL!=(musicFile=fopen(fileName,"r")))
			break;
		musicNum=i;
		int noteNum;
		fscanf(musicFile,"%d",&noteNum);
		notes[i]=(int*)malloc(sizeof(int)*(noteNum+1));
		times[i]=(double*)malloc(sizeof(double)*(noteNum+1));
		int *note=notes[i];
		double *time=times[i];
		note[0]=noteNum;
		for(int j=1;j<=noteNum;++j)
			fscanf(musicFile,"%d%lf",note+j,time+j);
	}
}

int main(void){
	init();
	int musicID=1;
	while(1){
		/*TODO
			检测按钮按下，切换乐曲
		*/
		play(notes[musicID],times[musicID]);
	}
}
