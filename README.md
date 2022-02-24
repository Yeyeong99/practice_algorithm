# practice_algorithm

|주언어|파이썬|
|:-:|:-|
|참고자료|- 이것이 취업을 위한 코딩 테스트다 with 파이썬<BR>- 파이썬 자료구조와 알고리즘: 기초 튼튼, 핵심 쏙쏙, 실력 쑥쑥<br>Do it! 자료구조와 함께 배우는 알고리즘 입문: 파이썬 |
|참고 사이트|- 백준<br>- 코드업<br>- 프로그래머스|
#
## 정리
|자료구조|구조|시간복잡도|의미|
|:-:|:-:|:-:|:-:|
|스택|LIFO|O(1)|배열의 끝에서만 데이터에 접근할 수 있는 선형 자료구조|
|큐|FIFO|O(1)|들어온 순서대로 접근이 가능한 자료구조|  
  
## 스택
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

## 큐
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
  
  # 0 번째가 뒤, 반대가 앞
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
  
```python

3. 스택 두 개 활용
