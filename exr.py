import discord
client = discord.client()
    async def on_message(message):
        message_list = message.content.lower()
        message_list = message_list.split()
        await message.channel.send("what workouts would you like to take part in ?. \n muscle building, weight loss, fitness ")



        if "1" in message_list:
            await message.channel.send("great!, you chosen muscle building lets get started")

            await message.channel.send("what body parts would you like to work today?. \n upperbody, lowerbody")
            msg1 = await client.wait_for('message')
            msg1_list = msg1.content.lower()
            msg1_list = msg1_list.split()


                if 'upperbody' in msg1_list:
                    await message.channel.send("12 close-grip barbel bench press x3 \n 10 chest dips x 3 \n 12 pectoral fly x 3")



            elif 'lowerbody' in ms1_list:
                    await message.channel.send('firstly strech out your muscles with a warm up for five minutes'

                if 'yes' in msg1_list:

                    await messsage.channel.send("For the first warm exercise position yourself in a squating position and carry out 15 reps(repetition) and then take ten seconds for a break. \n then afterwards repeat the same instructions three more times with a ten second break inbetween. ")
                    await message.channel.send("12 leg extensions x3, 12 dumbbell lunges x3, 12 squating with barbell bar x3 x 3, 12 ")


        elif "2" in message_list:
            await message.channel.send("great!, you chosen weight loss lets get started")
            await message.channel.send("Now we can begin with weight training. n\ Before we start we must at all costs avoid causing injuries to ourselves when training \n Do not train with weight which is straining when starting as this will cause will long lasting injury.")
            await message.channel.send("There will be six exercises which have been put together, this is: shoulder press, bicep curls, chest press, quad extension, kettlebell squat.\n carry this out these exercises out at a light weight, then do this 15 reps and 4 sets for each ")


        elif "3" in message_list:
            await message.channel.send("great!, you chosen fitness workout lets get started")
            await message.channel.send("would you like to take part in a High intesity or endurance code")
            msg3 = await client.wait_for('message')
            mgs3_list = msg3.content.lower()
            msg3_list = msg3_list.split()


            if message.content.lower().startswith('High'):
                    await High_message.channel.send('firstly we will have to strech out to prevent muscles being pulled. \n are you ready ?')
                    if 'yes' in msg3_list():

                        await message.channel.send("For the warm up exercise you will need to run at an incline angle on a treadmill, this will be done at a fast pace for 5 minutes.")
                        await message.channel = await for client.wait_for('finished')
                        await message.channel.send("Now we can begin this workout, the routines will be stairmaster on a fast speed for 10 minutes, bench press 4x6, squat 6x4, sit ups 20x3, plank for a minute x 3")
            elif message.content.lower().startswith('endurance'):
                    await endurance_message.channel.send('firstly we will have to strech out to prevent muscle being pulled. \n are you ready ?')
                    if 'yes' in msg3_list():
                        await message.send("For the warm up exercise you will have to row for 15 minutes. \n are you ready? ")
                        await message.channel = await for client.wait_for('finished')
                        await message.channel.send("Now we can begin the workout, this is the routine: treadmill 20 mins, cycling 20 mins, stair master.")
