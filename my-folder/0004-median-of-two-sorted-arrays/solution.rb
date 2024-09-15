# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Float}
def find_median_sorted_arrays(nums1, nums2)
  # dogs.bsearch_index { |dog| dog.age >= another_dog.age }
  small, big = [nums1, nums2].sort_by(&:size)
  # for each element in small > insert into big with binary search

  while !small.empty?
    x = small.pop
    # i = big.bsearch_index { |y| x < y } || -1
    if x > big.last
      big << x
    else
      i = bsearch_index(big, x)
      big.insert(i, x)
    end
  end

  p big

  if big.size.even?
    big[big.size / 2 - 1, 2].sum / 2.0
  else
    big[big.size / 2]
  end
end

def bsearch_index(arr, target)
  l, r = 0, arr.size - 1

  while l < r
    mid = l + (r - l) / 2
    if target < arr[mid]
      r = mid
    else
      l = mid + 1
    end
  end
  l
end
