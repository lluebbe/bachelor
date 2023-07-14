import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

counter = 0
file_path = "importantResults.json"
data = read_json_file(file_path)

for index, result in enumerate(data['assessmentResults']):
    resource = result['assessmentSubject']['resource']
    if 'virtualmachines' in resource:
        timestamp = data['assessmentResults'][index]['metadata']['timestamp']
        resource_id = data['assessmentResults'][index]['assessmentSubject']['resource']
        policy_definition_id = data['assessmentResults'][index]['importAssessmentPlan']['assessmentPolicy']
        is_compliant = data['assessmentResults'][index]['findings']['isCompliant']
        compliance_state = data['assessmentResults'][index]['findings']['complianceState']
        counter += 1

requirements = []

for i in range(counter):
    requirement = {
        "requirementId": "OPS-05.3H",
        "control": "PROTECTION AGAINST MALWARE – IMPLEMENTATION",
        "metricId": "MalwareProtectionOutput",
        "policyDefinitionId": policy_definition_id,
        "description": "This metric states whether automatic notifications are enabled (e.g. e-mail) about malware threats. This relates to EUCS’ definition of “continuous monitoring”.",
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
    json.dump(json_data, output_file, ensure_ascii=False, indent=4)
