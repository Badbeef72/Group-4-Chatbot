import discord


    async def on_message(message):
        message_list = message.content.lower()
        message_list = message_list.split()
        await message.channel.send("what workouts would you like to take part in ?. \n muscle building, weight loss, fitness ")



        if "1" in message_list:
            await message.channel.send("great!, you chosen muscle building lets get started")

            await message.channel.send("what body parts would you like to work today?. \n chest, back, legs, abs, shouders, arms")
            msg1 = await client.wait_for('message')
            msg1_list = msg1.content.lower()
            msg1_list = msg1_list.split()
            if 'chest' in msg1_list:
                await message.channel.send('firstly strech out your chest muscles with a warm up for five minutes\n are you ready ?')
                msg2 = await client.wait_for('message')
                msg2_list = msg2.content.lower()
                msg2_list = msg2_list.split()

                if 'yes' in msg1_list:

                    await.message.channel.send("For the first warm up exercise position yourself in a push up position and carry out 15 reps(repetition/push ups) and then take ten seconds.\n then afterwards repeat the same instructions three more times with a 10 second break inbetween. ")
                    await.message.channel.send("For your weight selection choose a weight which will be suitable to use for 36 reps.")
                    await.message.channel.send("12 close-grip barbel bench press x3 \n 10 chest dips x 3 \n 12 pectoral fly x 3")
                    await.message.channel.send("12 bench press x3 \n 10 incline bench press x3")


            if 'arms' in ms1_list:
                    await message.channel.send('firstly strech out your chest muscles with a warm up for five minutes\n are you ready ?')
                    msg3 = await client.wait_for('message')
                    msg3_list = msg3.content.lower()
                    msg3_list = msg3_list.split()

                if 'yes' in msg1_list:

                    await.messsage.channel.send("For the first warm exercise position yourself in a push up position and carry out 15 reps(repetition) and then take ten seconds for a break. \n then afterwards repeat the same instructions three more times with a ten second break inbetween. ")
                    await.message.channel.send("For your weight selection choose a weight which will be suitbale to use for 36 reps.")
                    await.message.channel.send("Biceps- 12 standing bicep cable curls x3, 12 dumbbell alternate bicep curls x3, 12 ez-bar curls x 3, 12 seated barbell curls x3")
                    await.message.channel.send("Triceps- 12 lying skull curshers x3, 12 cable tricep pushdown x3, 12 dumbbell overhead tricep extension x3, 6 close-grip barbell bench press x3. ")

                elif 'back' in msg1_list:
                    await message.channel.send('firstly strech out your ')

        elif "2" in message_list:
            await message.channel.send("great!, you chosen weight loss lets get started")

            await message.channel.send('what type of workout would you like to be involved in today? n\ weight training, cardio or High intesity work out?')
            msg4 = await client.wait_for('message')
            msg4_list = msg4.content.lower()
            msg4_list = msg4_list.split()


                if 'weight' in msg3_list':
                    await weight_message.channel.send('firstly we will have to strech out and not pull any muscles. \n are you ready ?')
                    if 'yes' in msg3_list():

                        await.message.channel.send("For the warm up exercises firstly grab a skipping rope and skip on the spot for one minute. \n Once you have done this take a twenty second break and repeat this exercise five times.")
                        await.message.channel = await for client.wait_for('finished')
                        await.message.channel.send("Now we can begin with weight training. n\ Before we start we must at all costs avoid causing injuries to ourselves when training \n Do not train with weight which is straining when starting as this will cause will long lasting injury.")
                        await.message.channel.send("There will be six exercises which have been put together, this is: shoulder press, bicep curls, chest press, quad extension, kettlebell squat.\n carry this out these exercises out at a light wieght, then do this 15 reps and 4 sets for each ")



                elif message.content.lower().startswith('cardio'):
                    await weight_message.channel.send('firstly we will have to strech out and try not to pull any muscle. \n are you ready ?')
                    if 'yes' in msg4_list():

                        await.message.channel.send("For the warm up exercises use a rowing machine and row for 5 minutes at the best speed you can. \n Once you have done this we will be ready to begin")
                        await.message.channel = await for client.wait_for('finished')
                        await.message.channel.send("Now we can begin the cardio routine. \n The workout routine will be running on the treadmil for 20 minutes at a fast pace. Once this is done you will need to take the stair master for 15 minutes. The final exercises will be cycling for 20 minutes at a high speed.")

                elif message.content.lower().startswith('High'):
                    await.cardio_message.channel.send('firstly we will have to strech out to try and not pull any muscles. \n are you ready ?')
                    if 'yes' in msg5_list():

                        await.message.channel.send("for the warm up exercise firstly. \n Carry out 20 press ups x4. \n once you have done this we will be ready to begin")
                        await.message.channel = await for client.wait_for('finished')
                        await.message.channel.send("Now we can begin the high intesity work out. \n You will need to carry out exercises at a fast pace. here is the exercies: mountain sprints 12x3, starjumps 12x3, press ups 12x3, crunchies 12x3, treadmill 10 mins at speed 7, overhead should presses 12x3")





        elif "4" in message_list:
            await message.channel.send("great!, you chosen fitness workout lets get started")
            await message.channel.send("would you like to take part in a High intesity or endurance code")
            msg5= await client.wait_for('message')
            mgs5_list = msg5.content.lower()
            msg5_list = msg5_list.split()



            if message.content.lower().startswith('High'):
                    await High_message.channel.send('firstly we will havre to strech out to prevent muscles being pulled. \n are you ready ?')
                    if 'yes' in msg6_list():

                        await.message.channel.send("For the warm up exercise you will need to run at an incline angle on a treadmill, this will be done at a fast pace for 5 minutes.")
                        await.message.channel = await for client.wait_for('finished')
                        await.message.channel.send("Now we can begin this workout, the routines will be stairmaster on a fast speed for 10 minutes, bench press 4x6, squat 6x4, sit ups 20x3, plank for a minute x 3")
            elif message.content.lower().startswith('endurance')
                    await endurance_message.channel.send('firstly we will have to strech out to prevent muscle being pulled. \n are you ready ?')
                    if 'yes' in msg7_list():

                        await.message.send("For the warm up exercise you will have to row for 15 minutes. \n are you ready? ")
                        await.message.channel = await for client.wait_for('finished')
                        await.message.channel.send("Now we can begin the workout, this is the routine: treadmill 20 mins, cycling 20 mins, stair master.")
