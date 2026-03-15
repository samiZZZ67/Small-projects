# Import required modules
# Die -> custom class that simulates a dice roll
# Bar and Layout -> used to create the bar chart
# offline -> used to generate the HTML plot locally

try:
    from die import Die
    from plotly.graph_objs import Bar, Layout
    from plotly import offline

except ImportError as e:
    print("Import error:", e)
    print("Make sure all required modules and files exist.")
else:
    try:
        # Create three 8-sided dice (D8)
        die_1 = Die(8)
        die_2 = Die(8)
        die_3 = Die(8)

        # Store results of all dice rolls
        results = []

        # Roll the dice 5000 times
        for roll_num in range(5000):
            result = die_1.roll() + die_2.roll() + die_3.roll()
            results.append(result)

        # Calculate the frequency of each possible result
        frequencies = []

        # Maximum possible result when rolling three dice
        max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides

        # Count how many times each result occurs
        for value in range(3, max_result + 1):
            frequency = results.count(value)
            frequencies.append(frequency)

    except Exception as e:
        print("Error during simulation:", e)

    else:
        try:
            # Create x-axis values (possible dice totals)
            x_values = list(range(3, max_result + 1))

            # Create bar chart data
            data = [Bar(x=x_values, y=frequencies)]

            # Configure axis titles
            x_axis_config = {'title': 'Result', 'dtick': 1}
            y_axis_config = {'title': 'Frequency of Result'}

            # Create chart layout
            my_layout = Layout(
                title="Results of rolling three D8 dice 5000 times",
                xaxis=x_axis_config,
                yaxis=y_axis_config
            )

            # Generate HTML visualization
            offline.plot({'data': data, 'layout': my_layout},
                         filename='three_d8_results.html')

            # Print frequency list in console
            print(frequencies)

        except Exception as e:
            print("Error while creating the visualization:", e)