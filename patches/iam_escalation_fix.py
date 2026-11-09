# Cloud-Security-Hardening: IAM Privilege Escalation Rule Validator
import re

def validate_iam_policy_statement(statement: dict) -> bool:
    """
    Validates IAM policy statements to eliminate false positives in privilege escalation checks
    by verifying explicit resource scoping and condition constraints.
    """
    actions = statement.get("Action", [])
    resources = statement.get("Resource", [])
    conditions = statement.get("Condition", {})
    
    # Normalize actions to a list
    if isinstance(actions, str):
        actions = [actions]
        
    # Known high-risk privilege escalation primitives
    escalation_primitives = ["iam:CreateAccessKey", "iam:PutUserPolicy", "iam:UpdateAssumeRolePolicy", "iam:CreatePolicyVersion"]
    
    has_risky_action = any(any(re.match(pattern.replace("*", ".*"), act) for pattern in escalation_primitives) for act in actions)
    
    if not has_risky_action:
        return False # Safe: No high-risk actions present
        
    # If wildcards are used on resources without strict conditions, flag as true positive risk
    if resources == "*" or (isinstance(resources, list) and "*" in resources):
        if not conditions:
            return True # True positive: Risky action with wildcard resource and no conditions
            
    return False # False positive mitigated by explicit resource scoping or condition guards
