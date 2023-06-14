#include <iostream>
int main(){
	std::string message1="czesc";
	int message_length1=message1.length();
	std::string message2="mniejsze";
	int message_length2=message2.length();
	std::string message3="wieksze";
	int message_length3=message3.length();
	std::string message4="wakanda";
	int message_length4=message4.length();
	int number=2;
	std::cout<<message1<<"\n";
	if(2<number){
		std::cout<<message2<<"\n";
		if(message_length2<11){
			std::cout<<message4<<"\n";
			}
		}
	if(2>number){
		number+=1;
		}

	return 0;
	}