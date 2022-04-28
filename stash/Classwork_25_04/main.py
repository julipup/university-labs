import search
import sort

if __name__ == "__main__":
  print('Search module:')
  print(search.linear_search([1,2,3,4,5], 4))
  print(search.binary_search([1,2,3,4,5,6], 4))
  print(search.substring_search("Hello there!", "nope"))

  print('Sort module:')
  print(sort.bubble_sort([5,4,3,2,1]))
  print(sort.selection_sort([5,4,3,2,1]))
  print(sort.insertion_sort([5,4,3,2,1]))