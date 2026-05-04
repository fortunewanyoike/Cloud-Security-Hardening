# Cloud Security Hardening: Linux Server Audit & Remediation

## 🛡️ Project Overview
This project focuses on the security hardening of a cloud-based **Apache Web Server** running on Linux. By conducting a comprehensive security audit using **Lynis**, identifying critical risks, and implementing a multi-layered remediation strategy, this project demonstrates the transition from a vulnerable default state to a hardened, production-ready environment aligned with **CIS Benchmarks** and **NIST** standards.

### 🎯 Objectives
- Conduct an automated security audit using **Lynis** to establish a baseline hardening index.
- Identify and remediate high-risk vulnerabilities, including unnecessary services (Samba) and unpatched packages.
- Implement a **Stateful Firewall Strategy** to enforce the Principle of Least Privilege (PoLP).
- Deploy and configure defensive tools such as **fail2ban** and **needrestart** to enhance system resilience.
- Develop a comprehensive **Incident Response Plan** and **Compliance Framework** (ISO 27001 / NIST).

---

## 🛠️ Technical Implementation & Audit Findings

### 1. Initial Security Baseline (Lynis Audit)
- **Hardening Index**: 59/100 (Initial).
- **Critical Findings**: 
  - Vulnerable and outdated kernel packages.
  - Active but unnecessary services (Samba on ports 139/445).
  - Lack of automated intrusion prevention and malware scanning.

### 2. Remediation & Hardening Actions
- **Service Minimization**: Purged **Samba** and other non-essential services to reduce the attack surface.
- **Package Management**: Applied full system updates and patches to address CVEs flagged during the audit.
- **Network Hardening**: Configured a restrictive firewall policy allowing only **HTTP (80)** and **HTTPS (443)** traffic.
- **Intrusion Prevention**: Deployed **fail2ban** to protect against brute-force attacks and **needrestart** to ensure service integrity after updates.

---

## 🔍 Governance & Compliance
This project aligns technical configurations with organizational governance:
- **IAM Policies**: Enforced strict User ID management (UID ≥ 1000) and Multi-Factor Authentication (MFA) recommendations.
- **Compliance Alignment**: Mapped hardening steps to **CIS Benchmarks** and **ISO 27001** control sets.
- **Incident Response**: Developed a 3-tier IR plan focusing on automated detection (log monitoring) and rapid isolation.

---

## 📈 Key Lessons & Reflections
A critical takeaway from this project was the need for **platform-specific adaptation**. For instance, container-level restrictions required a shift from local `iptables` to cloud-native security groups to achieve full firewall enforcement. This highlights the importance of understanding the underlying cloud infrastructure (AWS/Azure/GCP) when deploying security controls.

---

## 📝 Future Enhancements
- **Centralized SIEM Integration**: Exporting Lynis and fail2ban logs to a centralized dashboard for real-time security analytics.
- **Automated Scanning**: Implementing a CI/CD pipeline that automatically runs Lynis audits before each production deployment.

---
**Author**: Fortune Migwi Wanyoike  
**Role**: Junior Cybersecurity Engineer / Cloud Security Analyst  
**Technologies**: Linux (Ubuntu/Debian), Lynis, Apache, iptables, fail2ban, NIST Framework
