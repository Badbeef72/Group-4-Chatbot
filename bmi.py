# BMI calculator file.
import discord
import store
import random
client = discord.Client()

async def bmi_calculator(bmi_msg, height, weight):
    # Converts reply to an integer.
    bmi_height_int = float(height)
    bmi_weight_int = float(weight)
    # Calculates the BMI.
    bmi_result = bmi_weight_int / (bmi_height_int*bmi_height_int)
    await bmi_msg.channel.send('Your BMI is: ' + str(bmi_result))
    # Outputs result.
    if bmi_result < 18.5:
        await bmi_msg.channel.send('You are classified as underweight.')
    elif bmi_result >= 18.5 and bmi_result < 24.9:
        await bmi_msg.channel.send('You are classified as a healthy weight.')
    elif bmi_result >= 24.9 and bmi_result < 29.9:
        await bmi_msg.channel.send('You are classified as overweight.')
    elif bmi_result >= 29.9:
        await bmi_msg.channel.send('You are classified as obese.')
async def bmi_help(bmi_msg):
    await bmi_msg.channel.send("To help me calculate your bmi, you can type: bmi [your height in metres] [your weight in kilograms], and i'll do the rest for you!")
