bool f (int N) {for (int i = 1; i*i <= N ; i++) {if (N % i == 0) {return false;}}return true;}