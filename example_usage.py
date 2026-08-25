from client import LegalContractClauseRiskRedlineAnalyzerClient

def main():
    client = LegalContractClauseRiskRedlineAnalyzerClient()
    res = client.redline_enterprise_master_service_agreement('s3://contracts/Global_SaaS_MSA.docx', 'NEW_YORK')
    print('Legal Audit: ' + res['analysis_id'] + ' (Law: ' + res['governing_jurisdiction'] + ')')
    print('High Risk Clauses: ' + str(res['high_risk_clauses_detected']) + ' (Time Saved: ' + str(res['attorney_review_time_saved_pct']) + '%)')
    for r in res['redlined_sections']:
        print('  - [' + r['risk'] + '] ' + r['clause'] + ' -> ' + r['suggested_redline'])

if __name__ == '__main__':
    main()
