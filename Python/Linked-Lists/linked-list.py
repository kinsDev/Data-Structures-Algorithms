# So this is how Linked Lists are actually basically created.

head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
               "value": 7,
                "next": None
            }
        }
    }
}

print(head['next']['next']['value'])