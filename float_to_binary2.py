def float_to_binary(num):
  """Converts a float to its binary representation.

  Args:
    num: The float to convert.

  Returns:
    A string representing the binary representation of the float.
  """

  if num == 0:
    return "0"

  # Check if the number is negative
  is_negative = num < 0
  num = abs(num)

  # Get the integer part
  integer_part = int(num)
  binary_integer = bin(integer_part)[2:]

  # Get the fractional part
  fractional_part = num - integer_part
  binary_fractional = ""

  # Iterate until the fractional part becomes 0 or we reach 32 bits
  for i in range(32):
    fractional_part *= 2
    integer_part = int(fractional_part)
    binary_fractional += str(integer_part)
    fractional_part -= integer_part
    if fractional_part == 0:
      break

  # Combine the integer and fractional parts
  binary_representation = binary_integer + "." + binary_fractional

  # Add the sign if the number is negative
  if is_negative:
    binary_representation = "-" + binary_representation

  return binary_representation

# Example usage
number = 12.345
binary = float_to_binary(number)
print(binary)  # Output: 1100.01011000010100011110101110000101
