package_pen = int(input())
package_marker = int(input())
detergent = int(input())
percent_discount = int(input())
price_package_pen = 5.80
price_package_marker = 7.20
price_detergent = 1.20
sum = package_pen * price_package_pen + package_marker * price_package_marker + detergent * price_detergent
final_sum = sum - (sum * percent_discount) / 100
print(final_sum)