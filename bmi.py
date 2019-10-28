# BMI calculator file.
import discord
import store
import random
client = discord.Client()

async def bmi_calculator(bmi_msg):
    # Asks for height.
    await bmi_msg.channel.send('Certainly, may I ask what your height is, in centimetres?')
    # Converts reply to an integer.
    bmi_height = await client.wait_for('message')
    bmi_height_int = int(bmi_height.content)
    # Then, asks for weight.
    await bmi_msg.channel.send(random.choice(store.list_of_goods) + 'And may I ask what your weight in kilograms is?'.format(bmi_height))
    # Converts again to an integer.
    bmi_weight = await client.wait_for('message')
    bmi_weight_int = int(bmi_weight.content)
    # Calculates the BMI.
    bmi_result = (bmi_weight_int / (bmi_height_int**2)) / 100
    await bmi_msg.channel.send('Your BMI is: ' + str(bmi_result).format(bmi_weight))
    # Outputs result.
    if bmi_result < 18.5:
        await bmi_msg.channel.send('You are classified as underweight.')
    elif bmi_result >= 18.5 and bmi_result < 24.9:
        await bmi_msg.channel.send('You are classified as a healthy weight.')
    elif bmi_result >= 24.9 and bmi_result < 29.9:
        await bmi_msg.channel.send('You are classified as overweight.')
    elif bmi_result >= 29.9:
        await bmi_msg.channel.send('You are classified as obese.')
