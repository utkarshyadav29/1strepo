# Simple Voting System using basic Python functions

# Step 1: Create candidate list
candidates = ["saurabhi", "Tanishka", "Divyansh"]
votes = {candidate: 0 for candidate in candidates}

# To keep track of who has voted
voters = []

# Step 2: Define functions
def show_candidates():
    print("\nCandidates:")
    for i, candidate in enumerate(candidates, 1):
        print(f"{i}. {candidate}")

def vote():
    name = input("\nEnter your name: ").strip()
    if name in voters:
        print("⚠️ You have already voted!")
        return
    show_candidates()
    choice = int(input("Enter the number of your chosen candidate: "))
    if 1 <= choice <= len(candidates):
        selected_candidate = candidates[choice - 1]
        votes[selected_candidate] += 1
        voters.append(name)
        print(f"✅ Thank you, {name}! Your vote for {selected_candidate} has been recorded.")
    else:
        print("❌ Invalid choice!")

def show_results():
    print("\n📊 Voting Results:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")

    # Find winner
    winner = max(votes, key=votes.get)
    print(f"\n🏆 Winner: {winner} with {votes[winner]} votes!")

# Step 3: Main program
while True:
    print("\n--- Voting System ---")
    print("1. Vote")
    print("2. Show Results")
    print("3. Exit")
    option = input("Choose an option (1-3): ")

    if option == "1":
        vote()
    elif option == "2":
        show_results()
    elif option == "3":
        print("🛑 Voting session ended.")
        show_results()
        break
    else:
        print("❌ Invalid option! Please choose again.")
        
