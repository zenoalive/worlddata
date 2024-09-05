import tkinter as tk
from tkinter import ttk
import pandas as pd
import os

root = tk.Tk()
root.title("Health Data Selection")
# Get the current script directory
current_dir = os.path.dirname(__file__)

# Construct the path to the data file
data_file_path = os.path.join(current_dir, 'data/', 'for_2011_17_data.csv')
data_unemployment_male = os.path.join(current_dir, 'data/', 'fem_unemployment.csv')
data_unemployment_female = os.path.join(current_dir, 'data/', 'male_unemployment.csv')

# shape_file_path =  os.path.join(current_dir, '..', 'data/admin', 'ne_110m_admin_0_countries.shp')

# Load the data using the constructed path

# Load the data from the CSV file

# print(heights)

# def on_click():

df = pd.read_csv(data_file_path)   
country = df['Country'].unique()
# For height data
def on_height(country, gender):
   
# Extract the unique countries
   
    # heights = df['Mean height']
    
    type = health_var.get()
    if gender == 'Boys':
        genderOpp = 'Girls'
    if gender == 'Girls':
        genderOpp = 'Boys'
    # country_height = [df['Country'] == country]['Mean height'].values[0]
    
    othergender_data = df[df['Sex'] == genderOpp]
    print(f"Selected Country: {country}")
    print(f"Selected Gender: {gender}")
    print(f"Selected Type: {type}")

    # Filter the DataFrame to get the mean height for the selected country
    mean_height = df.loc[(df['Country'] == country) &(df['Sex'] == gender), 'Mean height'].values[0]
    samegender_data = df[df['Sex'] == gender]
    above_count = (samegender_data['Mean height'] > mean_height).sum()
    below_count = (samegender_data['Mean height'] < mean_height).sum()
    othergender_data = df[df['Sex'] == genderOpp]
    other_gender_above_count = (othergender_data['Mean height'] > mean_height).sum()
    other_gender_below_count = (othergender_data['Mean height'] < mean_height).sum()
    
    # Display the result (or you can use it further in your code)
    result_label.config(text=f"Mean Height for {country}'s {gender} is: {mean_height} cm")
    result_label1.config(text=f"{gender} of {above_count} countries have a higher mean height than {country}'s {gender}.")
    result_label2.config(text=f"{gender} of {below_count} countries have a lower mean height than {country}'s {gender}.")
    result_label3.config(text=f"{genderOpp} of {other_gender_above_count} countries have a higher mean height than {country}'s {gender}.")
    result_label4.config(text=f"{genderOpp} of {other_gender_below_count} countries have a lower mean height than {country}'s {gender}.")

def on_unemployment(country, gender):  
    if gender == 'Boys':
        genderOpp = 'Girls'
        df_same = pd.read_csv(data_unemployment_male)
        df_other = pd.read_csv(data_unemployment_female)
    if gender == 'Girls':
        genderOpp = 'Boys'
        df_same = pd.read_csv(data_unemployment_female)
        df_other = pd.read_csv(data_unemployment_male)
    # country_height = [df['Country'] == country]['Mean height']2019
    print(f"Selected Country: {country}")
    print(f"Selected Gender: {gender}")

    unemployment = df_same.loc[df['Country'] == country, 'unemployment'].values[0]
    # mean_height = df.loc[(df['Country'] == country) &(df['Sex'] == gender), 'Mean height'].values[0]

    above_count = (df_same['unemployment'] > unemployment).sum()
    below_count = (df_same['unemployment'] < unemployment).sum()
    other_gender_above_count = (df_other['unemployment'] > unemployment).sum()
    other_gender_below_count = (df_other['unemployment'] < unemployment).sum()
    
    # Display the result (or you can use it further in your code)
    result_label.config(text=f"Unemployment for {country}'s {gender} is: {unemployment} cm")
    result_label1.config(text=f"{gender} of {above_count} countries are more unemployed than {country}'s {gender}.")
    result_label2.config(text=f"{gender} of {below_count} countries are less unemployed than {country}'s {gender}.")
    result_label3.config(text=f"{genderOpp} of {other_gender_above_count} countries are more unemployed than {country}'s {gender}.")
    result_label4.config(text=f"{genderOpp} of {other_gender_below_count} countries are less unemployed than {country}'s {gender}.")

def on_submit():
    country = country_var.get()
    gender = gender_var.get()
    type = health_var.get()
    if (type == 'Height'):
        on_height(country, gender)
    if (type == 'Unemployment'):
        on_unemployment(country, gender)

# Convert it to a list (optional, if you need a list instead of a NumPy array)
country_list = country.tolist()
# height_list = heights.tolist()


country_var = tk.StringVar()
gender_var = tk.StringVar()
health_var = tk.StringVar()
# Create dropdowns
country_label = ttk.Label(root, text="Select Country:")
country_label.grid(column=0, row=0, padx=10, pady=10)
country_dropdown = ttk.Combobox(root, textvariable=country_var, values= country_list)
country_dropdown.grid(column=1, row=0, padx=10, pady=10)

gender_label = ttk.Label(root, text="Select Gender:")
gender_label.grid(column=0, row=2, padx=10, pady=10)
gender_dropdown = ttk.Combobox(root, textvariable=gender_var, values=["Boys", "Girls"])
gender_dropdown.grid(column=1, row=2, padx=10, pady=10)

health_label = ttk.Label(root, text="Select type:")
health_label.grid(column=0, row=3, padx=10, pady=10)
health_dropdown = ttk.Combobox(root, textvariable=health_var, values= ['Height', 'Weight', 'Unemployment', 'Sports Index'])
health_dropdown.grid(column=1, row=3, padx=10, pady=10)

#Click button 
# click_button = ttk.Button(root, text="Submit", command=on_submit)
# click_button.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Submit button
submit_button = ttk.Button(root, text="Submit", command=on_submit)
submit_button.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2, pady=10)
result_label1 = tk.Label(root, text="")
result_label1.grid(row=8, column=0, columnspan=2, pady=10)
result_label2 = tk.Label(root, text="")
result_label2.grid(row=10, column=0, columnspan=2, pady=10)
result_label3 = tk.Label(root, text="")
result_label3.grid(row=12, column=0, columnspan=2, pady=10)
result_label4 = tk.Label(root, text="")
result_label4.grid(row=14, column=0, columnspan=2, pady=10)
root.mainloop()
