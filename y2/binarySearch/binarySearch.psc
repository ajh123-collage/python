START
  FUNCTION binary_search(arr, low, high, x))
    IF high IS GREATER THAN low THEN
      SET mid TO (high + low) / 2
      IF arr[mid] IS x THEN
        RETURN mid
      ELSE-IF arr[mid] > x THEN
        RETURN binary_search(arr, low, mid-1, x)
      ELSE arr[mid] > x THEN
        RETURN binary_search(arr, low, mid+1, x)
      END-IF
    ELSE:
      RETURN -1
    END-IF
  END-FUNCTION

  SET arr TO [2, 3, 4, 10, 40]
  INPUT numberToFind

  SET result TO binary_search(arr, 0, LEGNTH OF(arr)-1, numberToFind)

  IF result NOT EQUAL TO -1 THEN
    OUTPUT result
  ELSE
    OUTPUT "Not found"
  END-IF  
END
