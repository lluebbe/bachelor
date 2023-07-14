import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

file_path = "sampleResponse.json"

data = read_json_file(file_path)

timestamps = []
resource_ids = []
policy_definition_ids = []
is_compliant_list = []
compliance_states = []

for item in data['value']:
    timestamp = item['timestamp']
    resource_id = item['resourceId']
    policy_definition_id = item['policyDefinitionId']
    is_compliant = item['isCompliant']
    compliance_state = item['complianceState']
    timestamps.append(timestamp)
    resource_ids.append(resource_id)
    policy_definition_ids.append(policy_definition_id)
    is_compliant_list.append(is_compliant)
    compliance_states.append(compliance_state)


assessment_results = []

for i in range(counter):

    metadata = {
        "timestamp": timestamps[i]
    }

    assessment_subject = {
        "resource": resource_ids[i],
    }

    assessment_plan = {
        "assessmentPolicy": policy_definition_ids[i],
    }

    finding = {
        "isCompliant": is_compliant_list[i],
        "complianceState": compliance_states[i]
    }

    assessment_result = {
        "metadata": metadata,
        "importAssessmentPlan": assessment_plan,
        "assessmentSubject": assessment_subject,
        "findings": finding
    }

    assessment_results.append(assessment_result)

json_data = {
    "assessmentResults": assessment_results
}

output_file_path = "importantResults.json"
with open(output_file_path, "w") as output_file:
    json.dump(json_data, output_file, indent=4)

print("Die Assessment-Ergebnisse wurden erflogreich in JSON-Format gespeichert")
