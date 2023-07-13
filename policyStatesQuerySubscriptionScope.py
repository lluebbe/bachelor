from azure.identity import InteractiveBrowserCredential
from azure.mgmt.policyinsights import PolicyInsightsClient
import json

def main():
    client = PolicyInsightsClient(
        credential=InteractiveBrowserCredential(),
        subscription_id="<subscription_id>",
    )

    response = client.policy_states.list_query_results_for_subscription(
        policy_states_resource="latest",
        subscription_id="<subscription_id>",
    )
    
    data = [item.as_dict() for item in response]

    output_json = {
        "@odata.nextLink": "",
        "@odata.context": "https://management.azure.com/subscriptions/<subscription_id>/providers/Microsoft.PolicyInsights/policyStates/$metadata#latest",
        "@odata.count": len(data),
        "value": data
    }
    output_file="policy_states_results.json"
    with open(output_file, "w") as file:
        json.dump(output_json, file,indent=4)
    print("Resultdaten wurden erflogreich in", output_file, "gespeichert.")
  
   
if __name__ == "__main__":
    main()
