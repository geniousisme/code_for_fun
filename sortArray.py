import random

class Solution:

      def __select_nth(self, n, items):
          pivot = random.choice(items)

          lesser = [item for item in items if item < pivot]
          if len(lesser) > n:
              return self.__select_nth(n, lesser)
          n -= len(lesser)

          numequal = items.count(pivot)
          if numequal > n:
              return pivot
          n -= numequal

          greater = [item for item in items if item > pivot]
          return self.__select_nth(n, greater)

      def __median(self, items):
          if len(items) % 2:
             return self.__select_nth(len(items)//2, items)
          else:
             left  = self.__select_nth((len(items)-1) // 2, items)
             right = self.__select_nth((len(items)+1) // 2, items)
          return (left + right) * 0.5
      
      def quirk_sort(self, nums):
          length   = len(nums)
          if length < 2:
             return nums
          new_nums = [0 for i in xrange(length)]
          median   = self.__median(nums) 
          odd_idx  = 1; even_idx = 0; i = 0
          for n in nums:
              if n <= median:
                 new_nums[even_idx] = n
                 even_idx += 2
              elif n > median:
                 new_nums[odd_idx] = n
                 odd_idx += 2
              i += 1
              if odd_idx > length - 1 or even_idx > length - 1:
                 break
          while even_idx < length:
                new_nums[even_idx] = nums[i]
                even_idx += 2
                i += 1
          while odd_idx  < length:
                new_nums[odd_idx]  = nums[i]
                odd_idx  += 2
                i += 1
          return new_nums

if __name__ == "__main__":
   s = Solution()
   print s.quirk_sort([1, 8, 2, 7, 4, 6, 5, 3])
   print s.quirk_sort([1, 8, 1])
   print s.quirk_sort([2, 2, 2, 2, 3])
   print s.quirk_sort([0, 1])



           