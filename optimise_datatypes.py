import pandas as pd
# find veh_class value counts

# read the clean_08 CSV
df = pd.read_csv("clean_08.csv")

df["veh_class"].value_counts()

# find city_mpg value counts
df.city_mpg.value_counts()

# Change city_mpg, hwy_mpg, cmb_mpg to be an int using .astype()
df["city_mpg"] = df["city_mpg"].astype("int8")
df["hwy_mpg"] = df["hwy_mpg"].astype("int8")
df["cmb_mpg"] = df["cmb_mpg"].astype("int8")

df[["city_mpg", "hwy_mpg", "cmb_mpg"]].describe()

# 	city_mpg	hwy_mpg	cmb_mpg
# count	987.000000	987.000000	987.000000
# mean	17.386018	24.038501	19.788247
# std	4.088018	4.753406	4.251565
# min	8.000000	13.000000	10.000000
# 25%	15.000000	20.000000	17.000000
# 50%	17.000000	24.000000	20.000000
# 75%	20.000000	27.000000	22.000000
# max	48.000000	45.000000	46.000000


# Check data types
print(df.dtypes)

# Check memory usage of each column
print(df.memory_usage(deep=True))

# Get total memory usage
print(f"Total memory usage: {df.memory_usage(deep=True).sum()} bytes")

# assign trans, drive, fuel, veh_class, and smartway to "category" using .astype()
df["trans"] = df["trans"].astype("category")
df["drive"] = df["drive"].astype("category")
df["fuel"] = df["fuel"].astype("category")
df["veh_class"] = df["veh_class"].astype("category")
df["smartway"] = df["smartway"].astype("category")