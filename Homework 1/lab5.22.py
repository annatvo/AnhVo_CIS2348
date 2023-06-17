# Anh Vo
# PSID: 2037824
# Lab 5.22

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

service1 = input('Select first service:\n')
service2 = input('Select second service:\n')

print("\nDavy's auto shop invoice\n")

if service1 == 'Oil change':
    service_price1 = 35
    print(f'Service 1: {service1}, ${service_price1}')
elif service1 == 'Tire rotation':
    service_price1 = 19
    print(f'Service 1: {service1}, ${service_price1}')
elif service1 == 'Car wash':
    service_price1 = 7
    print(f'Service 1: {service1}, ${service_price1}')
elif service1 == 'Car wax':
    service_price1 = 12
    print(f'Service 1: {service1}, ${service_price1}')
elif service1 == '-':
    service_price1 = 0
    print('Service 1: No service')

if service2 == 'Oil change':
    service_price2 = 35
    print(f'Service 2: {service2}, ${service_price2}\n')
elif service2 == 'Tire rotation':
    service_price2 = 19
    print(f'Service 2: {service2}, ${service_price2}\n')
elif service2 == 'Car wash':
    service_price2 = 7
    print(f'Service 2: {service2}, ${service_price2}\n')
elif service2 == 'Car wax':
    service_price2 = 12
    print(f'Service 2: {service2}, ${service_price2}\n')
elif service2 == '-':
    service_price2 = 0
    print('Service 2: No service\n')

print(f'Total: ${service_price1 + service_price2}')

