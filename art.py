import turtle

# Function to draw a circle
def draw_circle(radius):
    turtle.speed(0)  # Set the drawing speed to the fastest
    turtle.circle(radius)  # Draw the circle with the given radius
    turtle.hideturtle()  # Hide the turtle after drawing

# Get user input for the radius
radius = float(input("Enter the radius of the circle: "))

# Draw the circle
draw_circle(radius)

# Keep the window open until manually closed
turtle.done()
