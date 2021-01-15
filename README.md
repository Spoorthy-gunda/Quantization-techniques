# Quantization Techniques

### Why quantization?
With increase in ML application on all the edge devices like mobiles, laptops, smart watches and so on, there is a need to reduce the usage of computing and memory resources when these ML algorithms are used in the inference stage on these edge devices. Quantization maps bigger values to smaller values in such a way that the accuracy is not affected considerably.

In this project I explored different ways to quantize the weights to 16 bits, 8 bits, and 4 bits.

## 1. Scaling:
In this approach the the absolute maximum value from the weights is scaled to the highest value that can represented by the bits that are avialable. For example, for quantizing to 16 bits if m is the absolute maximum and b is the maximum value that can be represented by 15 bits, then the scaling factor is b/m. All the values are multiplied by this scaling factor. Note that 1 bit must be used for the sign of the value(+ or 1), hence 15 bits are used to represent the maximum.

## 2. Clipping:
In this approach instead of scaling the absolute maximum top 1 percentile value is found from the absolute values and is scaled to the highest value that can represented by the bits that are avialable. For example, let m be the top 1 percentile value and b the maximum value that can be reprsented then the scaling factor is b/m. There will be some weights that exceed b(or less than -b) after scaling which are set to b( or -b) hence the name cliping.

## Fixed-Point Representation:
In both of the above techniques discussed the weights are represented in floating point representation. Converting the floating point values to fixed point there is some loss of precision but the fixed point representation makes the computations much faster and needs less resources.
