## After Army Algorithm
___
#### 20.06.16
- BOJ 2588
  간단한 문제, input을 어떻게 사용하는 지 까먹은 내가 레전드.
  조금 더 잘 풀어볼 수 있을 거 같다.
#### 20.06.17
- BOJ 1330
  동시에 입력되는 두 수를 비교한 결과를 출력하는 문제,
  map 함수를 이용하여 아주 조금은 효율적으로 풀지 않았나 생각한다.
- BOJ 2753
  윤년인지 확인하는 문제, 단순히 문제에서 말해준 규칙을 if문으로 나열해 풀었다. 이게 최선인가?
#### 20.06.22
- BOJ 14681
  두 수를 입력받고 어느 사분면에 속하는 지 출력하는 문제, 변수를 사용하지 않고 if문에 input을 사용했다.
- BOJ 2884
  24시간 기준으로 45분을 뺀 시각을 출력하는 문제, 입력받은 분에 45를 뺀 값으로 비교를 했으며 0시 일 때를 따로 확인하여 23시로 바꿔주었다.
#### 20.06.23
- BOJ 5543
  5개의 수를 입력받고, 각 3개, 2개 중 제일 작은 수를 더한 값에 50을 뺀 값이 정답인 단순 구현문제, lambda를 쓸 생각은 했지만 접근 방법이 달랐던 것 같다. min 함수를 쓸 생각은 했다는 것에 일단 만족
- BOJ 2523
  입력받은 수까지 올라갔다가 다시 내려가는 별 찍기 문제, 처음엔 1부터 n까지, n에서 1까지의 range를 합치고 n이 1일 때를 예외처리 했다. ([,1] 이렇게 되기 때문)
  다른 풀이는 출력문에 + n * 절댓값(i)를 해주고 n-1 ~ -n 까지 -1되는 range를 만들었다.
  (n이 3일 때 [2,1,0,-1,-2])
  역시 별 찍기가 뇌를 깨우기 좋은 것 같다.
#### 20.06.24
- BOJ 10996
  별 찍기, 처음보는 유형의 별 찍기여서 상당히 헤맸다.
  찾은 규칙으로는 열의 수는 n*2인 것과 / 한 열에 별과 공백의 총 수는 n / 홀수열일 때 별으로 시작이였다.
  첫 풀이는 이를 가지고 이중 반복문으로 구현을 했다.
  다른 풀이는 나와 달리 반복문 한 개를 가지고 구현했는데 n을 2로 나눈 값을 가지고 구현했는데 조금 더 생각해보면 나도 생각할 수 있었을 것 같다. ~~화이팅~~
- BOJ 10818
  한 열에 여러 수를 입력받고 그 중 제일 큰 수와 작은 수를 출력하는 문제, min과 max를 사용해서 풂
- BOJ 1193
  입대 전에 풀었다가 실패한 문제, [위 글](https://wlstyql.tistory.com/53)을 참조하여 풀었으며 분모, 분자의 합과 stage + 1이 같다는 것을 이용하면 다르게도 풀 수 있을 것 같다.
#### 20.06.26
- BOJ 2562
  9가지의 수를 입력받고 그 중 재일 큰 수와, 그 수가 몇 번째로 입력 되었는 지 출력하는 문제.
  max를 이용하여 숏코딩을 할 수 있었지만 반복문을 한 번 사용하여 확인을 하는 것이 더욱 효율적이라 생각돼 이 방법을 택했다.
- BOJ 3052
  입력받는 10개의 수들을 42로 나눈 나머지 값이 겹치지 않게 몇 개인지 출력하는 문제.
  중복되는 요소가 없는 set 자료형을 이용하여 간편하게 풀었다.
#### 20.06.28
- BOJ 11650
  2차원 좌표를 받고 X 좌표가 증가하는 순으로 정렬, X 좌표가 같을 시 Y 좌표가 증가하는 순으로 정렬하여 출력하는 문제. 파이썬의 sort 메소드의 key를 lambda식을 사용해서 풀었다.
- BOJ 11651
  위 문제의 우선순위가 XY에서 YX로 바뀐 문제 lambda식을 바꿔서 풀었다.
- BOJ 15596
  list를 매개변수로 갖는 함수 solve는 list에 들은 모든 값을 더한 값을 반환해준다. 위 함수를 구현하는 문제. sum 메소드를 사용해서 간단히 풀었다.
#### 20.06.29
- BOJ 2798
  n과 m을 입력 받은 후, 길이가 n인 수들의 배열 l을 입력 받는다. l에 존재하는 수들 중 3개를 합친 값이 m이 넘지 않으며, m과 최대한 가까운 값을 구하는 문제. 3중 반복문을 이용하여 브루트포스 방법을 통해 풀었다.
#### 20.06.30
- BOJ 10828
  스택을 구현하는 문제이다. 처음엔 전역 변수 list, l과 함수들로 구현하였지만 백준 체점 도중 런타임 에러로 인하여 class로 스택을 구현하였으나 이 또한 백준 체점 도중 시간초과로 인해 input = sys.stdin.readline를 이용하여 시간을 단축시켰다. 풀이는 쉬웠으나 체점 기준에 맞추기 힘들었다.
#### 20.07.02
- BOJ 15719
  n과 1 ~ n-1까지 이루어진 수열을 입력받는 다. 수열에는 중복된 수가 한 개 존재하며, 그 것이 문제의 정답이다. 첫 풀이는 단순히 수열을 기준으로 반복문을 수행하고 dictionary에 key에 수열의 수를 넣어 이미 존재하는 수일 때 break하여 그 수를 출력하는 것으로 풀이를 하였으나 백준 체점 기준으로 메모리 초과 결과가 나와 검색해보니 sys.stdin.read()를 사용해야한다 ... 해서 사용해봤으나 EOF를 따로 입력해야하는 read() 특성상 마음대로 구현이 되지 않아 이 부분은 다른 분 풀이를 참고하여 read() 함수를 구현했다.
  read()를 참고하며 본 방법인데 중복된 문자는 1개, 1 ~ n-1까지의 수로 이루어진 수열이라는 특징을 이용해 __1 ~ n-1의 총 합(n*(n-1)//2)에서 수열에 존재하는 모든 수를 뺀 값에 -를 붙이면__+ 정답이 나오게 된다.. 역시 배울 게 남아도 너무 많이 남았다고 생각한다.
#### 20.07.03
- BOJ 1436
  666이 들어간 수 중에 n번째로 큰 수를 출력하는 문제. 브루트포스 방법으로 풀었다.
#### 20.07.05
- BOJ 15668
  숫자 n을 입력받고 n = n1 + n2 방식으로 표현할 때 n1과 n2에서 0~9까지 겹치는 수가 없는 경우를 출력하는 문제. 파이썬의 i "in" word와 같이 사용하는 메소드를 사용하여 풀었다. 첫 풀이에서 큰 수는 생각하지 못한체 반복문의 범위를 n//2+1으로 설정하여 시간초과가 나왔지만 range(1, min(100000, n))으로 바꾸었더니 정상적으로 정답을 맞을 수 있었다. 추가적으로 exit() 함수를 배웠다. 앞으로 유용하게 사용할 것 같다.
#### 20.07.06
- BOJ 13420
  숫자 n만큼 '2 + 2 = 4'와 같은 수식을 입력받고 정답이 맞을 때와 아닐 때 출력을 나눠 하는 문제. 문자열 형식을 실행하는 eval() 메소드를 이용하여 풀었다.
- BOJ 5524
  숫자 n만큼 대문자와 소문자가 섞여있는 문자열을 입력받고 모든 문자열을 소문자로 출력하는 문제. 문자열의 lower() 메소드를 이용하여 풀었다.
- BOJ 2935
  10의 제곱 형태인 두 수와 +, * 중 하나를 입력받고 연산된 수를 출력하는 문제. 첫 풀이에서는 연산 속도를 위해 * 일 때 두 수의 0을 세어 더한 값 A를 '1', '0' * A해서 풀었다. 두 번째 풀이는 eval을 이용하여 숏코딩 스타일로 풀었다.
