BÀI 1
#include<iostream>
using namespace std;

//hàm nhập  
void nhap(int *arr, int n) {
	//sử dụng vòng lặp để nhập phần tử thứ i 
	for (size_t i = 0; i < n; i++)
	{
		cout << "Nhập phần tử thứ[" << i << "] = ";
		cin >> arr[i];
	}
}
// Tìm max 
int Find_Max(int* arr, int n) {
	int max = arr[0];
    //dùng vòng lặp for để so sánh các số trong mảng 
	for (size_t i = 1; i < n; i++)
	{
		if (arr[i] > max) {
            //update lại max mới nhất  
			max = arr[i];
		}
	}
	return max;
}

int main() {
	int n; //số phần tử cho mảng 
	cout << "Nhap so phan tu mang: ";
	cin >> n;
	int* arr = new int[n]; //sử dụng mảng động 
	
	nhap(arr, n);
	int max = Find_Max(arr, n); // gọi hàm tìm gtr max

	cout << "MAX = " << max << endl;

	return 0;
}

BÀI 2
#include<iostream>
using namespace std;

int main (){
    string sodienthoai1 = "0983876207";
    string sodienthoai2 = "0918295063";
	int hour = 01;
	int minute = 18;
	int second = 25;
	cout << "Cuộc gọi từ " << sodienthoai1<<" đến "<<sodienthoai2<<
" với thời gian "<<hour<< ":" << minute<< ":" << second <<
" là: "<<((hour*60+ minute+ second/60)*1190); 

	return 0;
}
