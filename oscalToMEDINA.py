import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

file_path = "importantResults.json"
data = read_json_file(file_path)

timestamp =  data['assessmentResults'][0]['metadata']['timestamp']
resource_id = data['assessmentResults'][0]['assessmentSubject']['resource']
policy_definition_id = data['assessmentResults'][0]['importAssessmentPlan']['assessmentPolicy']
is_compliant = data['assessmentResults'][0]['findings']['isCompliant']
compliance_state = data['assessmentResults'][0]['findings']['complianceState']

requirements = []

requirement = {
    "requirementId": "OPS-05.3H",
    "control": "PROTECTION AGAINST MALWARE – IMPLEMENTATION",
    "metricId": "MalwareProtectionOutput",
    "policyDefinitionId": policy_definition_id,
    "description":"This metric states whether automatic notifications are enabled (e.g. e-mail) about malware threats. This relates to EUCS’ definition of “continuous monitoring”.",
    "timestamp": timestamp,
    "targetValue": is_compliant,
    "targetValueDescription": compliance_state,
    "targetValueDatatype": "Boolean",
    "intervalH": "1",
    "targetResourceType": "VirtualMachine",
    "targetResource": resource_id,
    "securityFeature": "malwareProtection.applicationLogging.loggingService"
}

requirements.append(requirement)

json_data = {
    "Metrics": requirements
}

output_file_path = "medinaMetric.json"
with open(output_file_path, "w", encoding='utf-8') as output_file:
    json.dump(json_data, output_file,ensure_ascii=False, indent=4)



    