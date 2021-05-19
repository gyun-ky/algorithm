#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int arr[9][9];
int box[10][10];
int rowValid[9][10];
int colValid[9][10];
int gameNum;

int valid_box(int row, int col)
{
    int divRow = row / 3;
    int divCol = col / 3;

    if (divRow == 0)
    {
        if (divCol == 0)
            return 1;
        else if (divCol == 1)
            return 2;
        else
            return 3;
    }
    else if (divRow == 1)
    {
        if (divCol == 0)
            return 4;
        else if (divCol == 1)
            return 5;
        else
            return 6;
    }
    else
    {
        if (divCol == 0)
            return 7;
        else if (divCol == 1)
            return 8;
        else
            return 9;
    }
}

int promising(int row, int col, int val)
{
    cout << "[" << row << "," << col << "] vall = " << val << endl;
    if (box[valid_box(row, col)][val] == 1)
    {
        cout << "같은 박스!" << endl;
        return 0;
    }

    if (rowValid[row][val] == 1)
    {
        cout << "같은 row" << endl;
        return 0;
    }

    if (colValid[col][val] == 1)
    {
        cout << "같은 col" << endl;
        return 0;
    }

    cout << "promising" << endl;
    return 1;
}

void printArr()
{
    for (int row = 0; row < 9; row++)
    {
        for (int col = 0; col < 9; col++)
        {
            cout << arr[row][col] << ' ';
        }
        cout << endl;
    }
}

void sudoku(int row, int col)
{
    if (arr[row][col] != 0)
    {
        if (row == 8 && col == 8)
        {
            cout << "여기옴" << endl;
            printArr();
            return;
        }
        else
        {
            if (col == 8)
            {
                sudoku(row + 1, 0);
            }
            else
            {
                sudoku(row, col + 1);
            }
        }
    }
    else
    {

        for (int i = 1; i <= 9; i++)
        {

            if (promising(row, col, i) == 1)
            {
                arr[row][col] = i;
                box[valid_box(row, col)][i] = 1;
                rowValid[row][i] = 1;
                colValid[col][i] = 1;

                if (row == 8 && col == 8)
                {
                    cout << "여기옴" << endl;
                    printArr();
                    exit(0);
                }
                else
                {
                    if (col == 8)
                    {
                        sudoku(row + 1, 0);
                    }
                    else
                    {
                        sudoku(row, col + 1);
                    }
                    arr[row][col] = 0;
                    box[valid_box(row, col)][i] = 0;
                    rowValid[row][i] = 0;
                    colValid[col][i] = 0;
                }
            }
        }
    }
}

int main()
{
    ifstream read;

    read.open("input.txt");
    if (read.is_open())
    {
        while (!read.eof())
        {

            memset(arr, 0, sizeof(arr));
            memset(box, 0, sizeof(box));
            memset(rowValid, 0, sizeof(rowValid));
            memset(colValid, 0, sizeof(colValid));

            int num = 0;
            read >> gameNum;

            for (int game = 0; game < gameNum; game++)
            {
                cout << "sudoku " << game + 1 << endl;
                for (int row = 0; row < 9; row++)
                {
                    for (int col = 0; col < 9; col++)
                    {
                        read >> num;
                        if (num != 0)
                        {
                            arr[row][col] = num;
                            box[valid_box(row, col)][num] = 1;
                            rowValid[row][num] = 1;
                            colValid[col][num] = 1;
                        }
                    }
                }
                cout << "시작전" << endl;
                printArr();
                cout<<"box"<<endl;
                for(int j=1; j<10; j++){
                    for(int k=1; k<10; k++)
                        cout<<box[j][k]<<' ';
                    cout<<endl;
                }
                cout<<"row"<<endl;
                for(int j=0; j<9; j++){
                    for(int k=1; k<10; k++)
                        cout<<rowValid[j][k]<<' ';
                    cout<<endl;
                }
                cout << "-------" << endl;
                sudoku(0, 0);
            }
        }
    }

    read.close();
}