# practice_algorithm


## 1. 참고자료
|주언어|파이썬|
|:-:|:-|
|참고자료|- 이것이 취업을 위한 코딩 테스트다 with 파이썬<BR>- 파이썬 자료구조와 알고리즘: 기초 튼튼, 핵심 쏙쏙, 실력 쑥쑥<br>Do it! 자료구조와 함께 배우는 알고리즘 입문: 파이썬 |
|참고 사이트|- 백준<br>- 코드업<br>- 프로그래머스|
#
## 2. 정리
  
|자료구조|시간복잡도|설명|
|:-:|:-:|:-|
|스택|O(1)|LIFO, 배열의 끝에서만 데이터에 접근할 수 있는 선형 자료구조|
|큐|O(1)|FIFO, 들어온 순서대로 접근이 가능한 자료구조|
|힙|O(1)/O(log n)|각 노드가 하위 노드보다 작은(큰) 이진 트리|
|해시|O(1)/O(n)|해시 함수를 통해 키, 값이 매핑됨. 해시 충돌이 일어날 경우 연결 리스트로 해결|

## 3. 자료구조
### 스택
배열의 끝에서만 데이터에 접근할 수 있는 선형 자료구조
1. 스택의 동작 - 모두 O(1)
  - push: 스택의 맨 끝에 항목을 삽입함
  - pop: 스택의 맨 끝 항복을 반환하고 동시에 제거
  - top/peek: 스택 맨 끝 항목을 조회
  - empty: 스택이 비어있는지 여부를 확인
  - size: 스택의 크기 확인
2. 파이썬에서의 스택
  - append, pop을 이용해 구현
  
   |![image](https://user-images.githubusercontent.com/67695343/154896601-6071c3bc-165d-4e5d-aa53-eeac6d0e3a54.png)|![image](https://user-images.githubusercontent.com/67695343/154896628-60906374-ec5f-45da-8b3a-8822a763290f.png)|
  |-|-|

  - 노드(객체)의 컨테이너로 스택 구현: [singly linked list](https://daimhada.tistory.com/105) 참고
  ```python
  class Node(object):
    def __init__(self, value=None, pointer=None):
      self.value = value
      self.pointer = pointer

  class Stack(object):
    def __init__(self):
      self.head = None
      self.count = 0

    def isEmpty(self):  
      return not bool(self.head)

    def push(self, item):
      self.head = Node(item, self.head) 
      # 새로 들어온 item이 head가 되고, 새로 들어온 item의 pointer는 기존의 head를 가리키게 되는 것. 
      # value = item, pointer = self.head
      self.count += 1

    def pop(self):
      if self.count > 0 and self.head:
        node = self.head
        self.head = node.pointer
        self.count -= 1
        return node.value
      else:
        print("Stack is Empty")

    def peek(self):
       if self.count > 0 and self.head:
         return self.head.value
       else:
         print("Stack is Empty")

    def size(self):
      return self.count

    def _printList(self):
      node = self.head
      while node:
        print(node.value, end=" ")
        node = node.pointer
        print()
  ```
  - 깊이 우선 탐색에서 유용하게 쓰임
3. collections.deque를 사용해 고정 길이 스택 클래스 구현
  ```python
  from typing import Any
  from collections import deque
  
  class Stack:
    """고정 길이 스택 클래스(collections.deque 활용"""

    def __init__(self, maxlen: int = 256) -> None:
      self.capacity = maxlen
      self.__stk = deque([], maxlen)

    def __len__(self) -> int:
      #스택에 쌓여있는 데이터 개수를 반환
      return len(self.__stk)

    def is_empty(self) -> bool:
      return not self.__stk

    def is_full(self) -> bool:
      return eln(self.__stk) == self.__stk.maxlen

    def push(self, value: Any) -> None:
      self.__stk.append(value)

    def pop(self) -> Any:
      return self.__stk.pop()

    def peek(self) -> Any:
      return self.__stk[-1]

    def clear(self) -> None:
      self.__stk.clear()

    def find(self, value: Any) -> Any:
      try:
        return self.__stk.index(value)
      except ValueError:
        return -1

    def count(clear, value: Any) -> int:
      return self.__stk.count(value)

    def __contains_(self, value: Any) -> bool:
      return self.count(value)

    def dump(self) -> int:
      print(list(self.__stk))
   ```

### 큐
들어온 순서대로 접근이 가능한 자료구조
배열의 인덱스 접근이 제한 됨
1. 동작 - 시간복잡도는 모두 O(1)
  - enqueue: 큐 뒤쪽에 항목을 삽입한다.
  - dequeue: 큐 앞쪽의 항목을 반환하고, 제거한다.
  - peek/front: 큐 앞쪽의 항목을 조회한다.
  - empty: 큐가 비어있는지 확인
  - size: 큐의 크기 확인
  
> 링 버퍼ring buffer: 배열의 맨 끝 원소(rear) 뒤에 맨 앞의 원소(front)가 연결되는 자료 구조 
  
2. 시간 복잡도가 O(n)인 경우 (insert를 사용해 모든 요소가 메모리 상에서 이동할 가능성이 있기 때문)
```python
  class Queue(object):
    def __init__(self):
      self. items = []
  
    def isEmpty(self):
      return not bool(self.items)

    # 0 번째가 rear(데이터를 넣는 쪽), 반대가 front(데이터를 꺼내는 쪽)
    def enqueue(self, item):
      self.items.insert(0, item)

    def dequeue(self):
      value = self.items.pop()
      if value is not None:
        return value
      else:
        return -1

    def size(self):
      return len(self.items)

    def peek(self):
      if self.items:
        return self.items[-1]
      else:
        return -1

    def __repr__(self):
      return repr(self.items)
  
```

3. 스택 두 개 활용
  - enqueue: inbox에 요소를 넣음. 이때 append 활용
  - dequeue
    - outbox에서 요소를 뺌.
      - 이때 outbox에 요소가 없으면 inbox에 있던 걸 pop해서 옮겨줌
        - 따라서 inbox에 들어있는 요소와 outbox에 들어있는 요소는 순서가 반대임(inbox가 위에서부터 1, 2, 3이라고 하면 outbox는 위에서부터 3, 2, 1)
      - 요소가 있으면 pop을 이용해 반환, 제거
      
```python
  class Queue(object):
    def __init__(self):
      self.in_stack = []
      self.out_stack = []
    
    def _transfer(self):
      while self.in_stack:
        self.out_stack.append(self.in_stack.pop())
    
    def enqueue(self, item):
      return self.in_stack.append(item)
    
    def dequeue(self):
      if not self.out_stack:
        self._transfer()
      if self.out_stack:
        return self.out_stack.pop()
      else:
        return -1
    
    def size(self):
      return len(self.in_stack) + len(self.out_stack)
    
    def peek(self):
      if not self.out_stack:
        self._transfer()
      if self.out_stack:
        return self.out_stack[-1]
      else:
        return -1
  
    def __repr__(self):
      if not self.out_stack:
        self._transfer()
      if self.out_stack:
        return repr(self.out_stack)
      else:
        return -1
  
    def isEmpty(self):
      return not (bool(self.in_stack) or bool(self.out_stack))
```
### 데크
스택과 큐의 결합체
- 양쪽 끝에서 항목의 조회, 삽입, 삭제 가능
- collections의 deque 모듈을 이용해 효율적으로 구현 가능
  - deque의 rotate(n): 음수면 왼쪽으로, 양수면 오른쪽으로 n만큼 shift
  
### 우선순위 큐
각 항목마다 우선순위 존재, 두 항목의 우선순위가 같을 경우 큐의 순서를 따름
- 힙을 이용해 구현
  
#### 힙
각 노드가 하위 노드보다 작은 이진 트리
- 리스트에서 가장 작은 요소에 반복적해서 접근하는 프로그램에 유용함
- 가장 작은 / 큰 요소를 처리하는 시간복잡도는 O(1)
- 추가, 조회, 수정을 처리하는 시간복잡도는 O(log n)
  
#### heapq 모듈
- heapq.heapify(list): O(n) 시간에 리스트를 힙으로 변환 가능

### 연결 리스트
값과 다음 노드에 대한 포인터가 포함된 노드로 이뤄진 선형 리스트
  
### 해시 테이블
1. 키를 값에 연결, 하나의 키가 0-1개의 값과 연관됨
- 해시 함수 필요
- 해시 버킷의 배열로 구성: 두 개의 키가 동일한 버킷에 해시될 경우 해시 충돌(hash collision)이 발생할 수 있음

2. 해시 충돌 해결 방법
- 각 버킷에 연결 리스트를 저장

3. 시간복잡도
- 조회, 삽입, 삭제: O(1)
- 충돌이 발생할 경우: O(n)
  
  
## 4. 알고리즘
### 1. 그리디 알고리즘
[이것이 취업을 위한 코딩테스트다](http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791162243077)의 내용 정리
1. 기본 원리
- 현재 상황에서 지금 당장 좋은 것만 고르는 방법
2. 특징
- 현재 내린 선택이 나중에 미칠 영향은 고려하지 않음
- 코딩테스트에서 암기 없이 풀 수 있는 가능성이 높음
> 다익스트라의 경우 암기가 필요한 그리디 알고리즘

- 문제 출제의 폭이 넓음
  - 문제 해결을 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요함
  - 최소한의 아이디어 + 아이디어의 정당성 여부 검토
- 정렬 알고리즘과 같이 출제되는 경우가 많음
  - ex)  가장 큰 순서대로 / 가장 작은 순서대로와 같은 기준을 제시함
3. 정당성
- 대부분의 경우 그리디 알고리즘으로는 최적의 해를 찾을 수 없음 
- 탐욕적으로 문제에 접근할 경우 정확한 답을 찾을 수 있다는 보장이 있으면 매우 효과적이고 직관적
  - ex) 동전 문제: 가지고 있는 동전 중 큰 단위가 항상 작은 단위의 배수일 경우
  
> ✔✔✔🤔
문제 유형 파악이 바로 되지 않을 경우 그리디 알고리즘 의심하기 
