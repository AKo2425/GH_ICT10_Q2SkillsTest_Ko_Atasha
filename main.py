main.py from pyscript import document

clubs = {
    "Drama Club": {
        "Description": "A club for drama lovers of all skill levels.",
        "Meeting Time": "Every Wednesday 3:30–5:00 PM",
        "Location": "Room 405",
        "Moderator": "Mr. De Guzman",
        "Number of Members": 20,
        "Category": "Performing Arts"
    },
    "Tennis Club": {
        "Description": "For students who enjoy the heat of the sun and sports.",
        "Meeting Time": "Every Friday 2:00–3:30 PM",
        "Location": "Room 210",
        "Moderator": "Mr. Gervacio",
        "Number of Members": 16,
        "Category": "Sports"
    },
    "Swimming Club": { 
        "Description": "Learn swimming techniques and enjoy pool activities.",
        "Meeting Time": "Every Thursday 3:00–4:30 PM",
        "Location": "School Pool",
        "Moderator": "Ms. Libramonte",
        "Number of Members": 18,
        "Category": "Sports"
    }
}

def show_info(e):
    selected = document.getElementById("clubSelect").value
    club = clubs[selected]

    text = f"""
    <h3 class='club-title'>{selected}</h3>
    <p><strong>Description:</strong> {club["Description"]}</p>
    <p><strong>Meeting Time:</strong> {club["Meeting Time"]}</p>
    <p><strong>Location:</strong> {club["Location"]}</p>
    <p><strong>Moderator:</strong> {club["Moderator"]}</p>
    <p><strong>Number of Members:</strong> {club["Members"]}</p>
    """

    document.getElementById("output").innerHTML = text

