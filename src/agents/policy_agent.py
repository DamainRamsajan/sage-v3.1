class PolicyAgent:  
    def sense(self, pheromone):  
        return pheromone.get("intensity", 0) * 0.9  # Trust-weighted  

    def act(self):  
        return {"type": "policy_delta", "intensity": 0.7}  

if __name__ == "__main__":  
    agent = PolicyAgent()  
    print(agent.act())  # Test output  