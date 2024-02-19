
# split the value using decimal point as seperator
# value = 4.25
# str_value = str(value)
# seperated_list = str_value.split('.')
# print(seperated_list)
# intregal_part, fractional_part = seperated_list[0], seperated_list[1]
# print(intregal_part)

def decompose_real_number(value):
    str_value = str(value)
    seperated_list = str_value.split('.')
    intregal_part, fractional_part = seperated_list[0], seperated_list[1]
    return intregal_part, fractional_part

def convert_string_to_float(fractional_part):
    floating_value = '0.' + fractional_part
    return float(floating_value)


# Example usage:
intregal_part, fractional_part = decompose_real_number(4.25)
print(intregal_part)
print(fractional_part)
dec = convert_string_to_float(fractional_part)
bit_string = ''
whole, dec = decompose_real_number(2 * dec)
bit_string += whole
print(bit_string)
dec = convert_string_to_float(dec)
whole, dec = decompose_real_number(2 * dec)
bit_string += whole
print(bit_string)

# Iterate the number of times, we want
# the number of decimal places to be
bits = bin(int(intregal_part)) + '.' + bit_string
print(bits)

bit_vector = [0]*32
print(bit_vector)

value = -255.3445
value = str(value)
whole_num = fraction = 0
print(value[0])
if value[0] == '-':
    bit_vector[0] = 1
    new_value = value[1:]
else:
    new_value = value
print(bit_vector)
# print(len(value))
whole_num, fraction = new_value.split('.')
print(whole_num)
whole_num_bits = bin(int(whole_num))
print(whole_num_bits)
for i in range(len(whole_num_bits[2:])):
    bit_vector[1 + i] = whole_num_bits[2 + i]
print(bit_vector)


def float_to_bits(f):
  """Converts a float to its binary representation.

  Args:
    f: The float to convert.

  Returns:
    A string containing the binary representation of the float.
  """

  # Get the binary representation of the float as a string.
  binary = bin(int(f * 2**52))[2:]

  # Add the sign bit.
  if f < 0:
    binary = "1" + binary
  else:
    binary = "0" + binary

  # Add the exponent bits.
  exponent = int(f.as_integer_ratio()[1]) - 1023
  exponent_binary = bin(exponent + 1023)[2:].zfill(11)
  binary = binary[:1] + exponent_binary + binary[1:]

  # Add the mantissa bits.
  mantissa_binary = f.as_integer_ratio()[0] % 2**52
  mantissa_binary = bin(mantissa_binary)[2:].zfill(52)
  binary = binary[:12] + mantissa_binary + binary[12:]

  return binary

# Example usage
f = -3.14159
binary = float_to_bits(f)
print(binary)
print(len(binary))
