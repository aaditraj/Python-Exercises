# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.
# Desired Output:
# 0.8475
rando = "X-DSPAM-Confidence:0.8475"
loc_str = rando.find('0')
ext_str = rando[loc_str:]
flt_str = float(ext_str)
print(flt_str)
