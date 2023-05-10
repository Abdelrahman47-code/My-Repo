#include<bits/stdc++.h>
counter = 0
s = int(input("Enter thr sum of numbers: "))

for x in range(s):
    y = 0
    z = s-x+1
    for y in range (z):
        z -= 1
        counter += 1
        res = x+y+z
        
        print(str(x)+' '+str(y)+' '+str(z))
        print(res)
        print(10*'*')
    print()
print("The number of different values: ", counter+1)

####################################

int counter = 0;
int s;
std::cout << "Enter the sum of numbers: ";
if (!(std::cin >> s)) {
    std::cerr << "Error: Invalid input. Please enter an integer." << std::endl;
    return 1;
}
if (s < 3) {
    std::cerr << "Error: The sum must be at least 3." << std::endl;
    return 1;
}

####################################

for (int x = 0; x < s; x++) {
    for (int y = x; y < s; y++) {
        int z = s - x - y;
        if (z < y) break;
        counter++;
        int res = x + y + z;
        
        std::cout << x << ' ' << y << ' ' << z << std::endl;
        std::cout << res << std::endl;
        std::cout << "**********" << std::endl;
    }
    std::cout << std::endl;
}
std::cout << "The number of different values: " << counter << std::endl;

####################################

int main() {
  for (int i = 1; i < 20; i += 2) {
    cout << string((50 - i * 2) / 2, ' ');
    cout << string(i * 2, '*');
    cout << endl;
  }

  for (int i = 19; i > 0; i -= 2) {
    cout << string((50 - i * 2) / 2, ' ');
    cout << string(i * 2, '*');
    cout << endl;
  }

  for (int i = 1; i < 14; i += 2) {
    cout << string((50 - i * 2) / 2, ' ');
    cout << string(i * 2, '*');
    cout << endl;
  }

  return 0;
}

####################################

int main (){
    int n,p,z,y;
    cin >> n;
    p = y = n/2;
    z = n-1;
    
    if (n%2==0){
        for (int x=0; x<p; ++x)
        {
            cout << string(x, ' ') << '*' << string(z, ' ')  << "*" << "\n";
            z -= 2;
        } 
        for (int x=1; x<=n; x+=2)
        {
            --y;
            cout << string(y, ' ') << '*' << string(x, ' ')  << "*" << "\n";
        } 
    } else 
        {
            for (int x=0; x<p; ++x)
            {
                cout << string(x, ' ') << '*' << string(z, ' ')  << "*" << "\n";
                z -= 2;  
            }
            for (int x=2; x<=n; x+=2)
            {
                --y;
                cout << string(y, ' ') << '*' << string(x, ' ')  << "*" << "\n";
            } 
        } return 0;
}



