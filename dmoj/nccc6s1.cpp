#include <iomanip>
#include <stdio.h>

using namespace std;

int main()
{
    int classes;
    double marks, temp;
    scanf("%d", &classes);
    for (int i = 0; i < classes; i++) {
        scanf("%lf", &temp);
        marks += temp;
    }
    printf("%.1lf\n", marks / classes);
    return 0;
}