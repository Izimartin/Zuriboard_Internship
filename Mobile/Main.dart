
// A program that prints odd numbers between 1 and 30

void main() 
{
  var odd = [];
  for(int i= 0; i <= 30; i++) {
    if(i%2!=0) {
      odd.add(i);
    }
    if(i==30) {
      print('The number is at $i');
      for(int n in odd) {
        print(n);
      }
    }
  }
}