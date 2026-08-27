import threading
import time

# -----------------------------------
# Lists
# -----------------------------------

titles = [
    "Harry Potter",
    "Pride and Prejudice"
]

pages = [
    250,
    430
]

first_name = [
    "J.K.",
    "Jane"
]

last_name = [
    "Rowling",
    "Austen"
]

locations = [
    "UK",
    "UK"
]

# -----------------------------------
# Build Nested Dictionary
# -----------------------------------

def build_book_dict(
        titles,
        pages,
        first_name,
        last_name,
        locations):

    inputs = zip(
        titles,
        pages,
        first_name,
        last_name,
        locations
    )

    d = {}

    for (
        title,
        page,
        first,
        last,
        location
    ) in inputs:

        d.update({

            title: {

                "Pages": page,

                "Author": {

                    "First": first,

                    "Last": last
                },

                "Publisher": {

                    "Location": location
                }
            }
        })

    # delay execution 3 seconds
    time.sleep(3)

    return d


# -----------------------------------
# Timer Function
# -----------------------------------

def timer_function():

    print(
        build_book_dict(
            titles,
            pages,
            first_name,
            last_name,
            locations
        )
    )


# -----------------------------------
# Test Build Dictionary
# -----------------------------------

print("Testing Function\n")

print(
    build_book_dict(
        titles,
        pages,
        first_name,
        last_name,
        locations
    )
)

# -----------------------------------
# Create Timer
# -----------------------------------

timer = threading.Timer(
    5.0,
    timer_function
)

timer.start()

print("\nTimer Created")

timer.cancel()

print("Timer Cancelled")