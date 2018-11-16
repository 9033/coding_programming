# Greedy Gift Givers
<pre>
문자열로 인덱스를 만들고 사용하면 됨
</pre>
```c
#include<stdio.h>
#include<string.h>
char names[10][15];
char name[15];
int money[10];
int mp;
main(){
	FILE *in=fopen("gift1.in","r");
	FILE *out=fopen("gift1.out","w");
	int x,y,z;
	int mon,p;
	fscanf(in,"%d",&mp);
	for(x=0;x<mp;x++)
		fscanf(in,"%s",names[x]);
	for(x=0;x<mp;x++){
		fscanf(in,"%s %d %d",name,&mon,&p);
		if(mon!=0){
			for(y=0;y<mp;y++)
				if(!strcmp(name,names[y])){
					money[y]-=(int)(mon/p)*p;
					break;
				}

			for(z=0;z<p;z++){
				fscanf(in,"%s",name);
				for(y=0;y<mp;y++)
					if(!strcmp(name,names[y]))
						money[y]+=(int)mon/p;
			}
		}
		else
			for(z=0;z<p;z++)
				fscanf(in,"%s",name);
	}
	for(x=0;x<mp;x++)
		fprintf(out,"%s %d\n",names[x],money[x]);
	return 0;
}
```

<pre>
div_t div(int,int) 는 몫과 나머지를 리턴.
특징은 cpu가 지원하는 경우 몫과 나머지를 같이 구한다고 한다.
형변환을 이용해서 정수변환하는 부분을 div를 사용하는 것으로 바꿈.
2015-09-05
</pre>
```c
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char names[10][15];
char name[15];
int money[10];
int mp;
main(){
	FILE *in=fopen("gift1.in","r");
	FILE *out=fopen("gift1.out","w");
	int x,y,z;
	int mon,p;
	fscanf(in,"%d",&mp);
	for(x=0;x<mp;x++)
		fscanf(in,"%s",names[x]);
	for(x=0;x<mp;x++){
		fscanf(in,"%s %d %d",name,&mon,&p);
		if(mon!=0){
			div_t g;
			g = div(mon,p);
			for(y=0;y<mp;y++)
				if(!strcmp(name,names[y])){
					money[y]-=mon-g.rem;
					break;
				}

			for(z=0;z<p;z++){
				fscanf(in,"%s",name);
				for(y=0;y<mp;y++)
					if(!strcmp(name,names[y]))
						money[y]+=g.quot;
			}
		}
		else
			for(z=0;z<p;z++)
				fscanf(in,"%s",name);
	}
	for(x=0;x<mp;x++)
		fprintf(out,"%s %d\n",names[x],money[x]);
	return 0;
}
```

<pre>
map을 사용해서 사람이름과 돈을 짝지은 값이 들어가게 하고, 사람이름을 검색해서 값을 수정하게 함.
출력할때 사람의 목록이 들어온 순서대로 출력을 해야 함. 그래서 vector를 이용해서 순서를 기억하고 그 순서대로 출력.
2015-09-05
</pre>
```cpp
#include<fstream>
#include<string>
#include<vector>
#include<unordered_map>
main(){
	std::fstream fin("gift1.in", std::fstream::in);
	std::fstream fout("gift1.out", std::fstream::out);
	int NP;
	fin >> NP;
	std::string name;
	std::unordered_map<decltype(name), int> p;
	std::vector<decltype(name)> names;
	for (int i = NP; i;i--) {
		fin >> name;
		p.insert({ name,0 });
		names.push_back(name);
	}
	for (int i = NP; i; i--) {
		int money, ap;
		fin >> name >> money >> ap;
		div_t g = {};
		if (money && ap)
			g = div(money, ap);
		auto chmoney = [&](int chm) {
			p.find(name)->second += chm;
		};
		chmoney(-(money - g.rem));
		for (int j = ap; j; j--) {
			fin >> name;
			chmoney(g.quot);
		}
	}
	for (auto& x : names) {
		auto h = p.find(x);
		fout << h->first << " " << h->second << std::endl;
	}
}
```