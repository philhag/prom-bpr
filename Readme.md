Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE) 2.4

# PROM-BPR

## Metadata
* **IRI**
  * `https://w3id.org/prom-bpr`
* **Creators(s)**
  * [Dr. Judith Fauth](https://orcid.org/0000-0002-9078-8393)
    [[ORCID]](https://orcid.org/0000-0002-9078-8393)
    (<judith.fauth@rub.de></a>) of [Technical University of Munich, DE](https://www.linkedin.com/in/judith-fauth-5b5137bb)
  * [Dr. Philipp Hagedorn](https://orcid.org/0000-0002-6249-243X)
    [[ORCID]](https://orcid.org/0000-0002-6249-243X)
    (<philipp.hagedorn-n6v@rub.de></a>) of [Ruhr University Bochum, DE](https://www.inf.bi.ruhr-uni-bochum.de/iib/lehrstuhl/mitarbeiter/philipp_hagedorn.html.en)
  * [Prof. Dr. Ronny Weinkauf](https://orcid.org/0009-0003-6827-0154)
    [[ORCID]](https://orcid.org/0009-0003-6827-0154)
    (<ronny.weinkauf@hs-merseburg.de></a>) of [Merseburg University of Applied Sciences, DE](https://www.hs-merseburg.de/hochschule/information/personenverzeichnis/details/person/weinkauf-ronny-613/)
* **Imports**
  * [http://www.w3.org/ns/prov-o#](http://www.w3.org/ns/prov-o#)
  * [https://w3id.org/ontobpr](https://w3id.org/ontobpr)
* **Ontology RDF**
  * RDF ([prom-bpr.ttl](turtle))

* **License**
  * The ontology is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. See the [`LICENSE`](LICENSE) file.
  
### Description
<p>PROM-BPR provides a reference process model for building permit review processes, capturing the key activities, their sequence, and dependencies for implementing process mining approaches. Furthermore, it contains classes for representing event log entries, unclassified event log entries, and event log compounds. The prefix of the ontology is <code>prom-bpr:</code>. The process model consists of three main phases: <code>prom-bpr:A_1_PrePhase</code>, <code>prom-bpr:A_2_ReviewPhase</code>, and <code>prom-bpr:A_3_PostPhase</code>. The ontology extends <code>ontobpr:</code> and utilizes <code>prov:</code>.</p>


## Table of Contents
1. [Classes](#classes)
1. [Object Properties](#objectproperties)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Classes
[Administrative check](#Administrativecheck),
[Applicant presents building application](#Applicantpresentsbuildingapplication),
[Archiving](#Archiving),
[Assignment (to plan checker)](#Assignment(toplanchecker)),
[Building / technical review](#Building/technicalreview),
[Building committee meeting](#Buildingcommitteemeeting),
[Check participation statements](#Checkparticipationstatements),
[Check stamps, payment](#Checkstamps,payment),
[Check/ request payment of taxes and fees](#Check/requestpaymentoftaxesandfees),
[Compile application request requirement list](#Compileapplicationrequestrequirementlist),
[Completeness check](#Completenesscheck),
[Completing documentation](#Completingdocumentation),
[Construction completion (notification)](#Constructioncompletion(notification)),
[Construction law review](#Constructionlawreview),
[Consultation with applicant](#Consultationwithapplicant),
[Content check](#Contentcheck),
[Content check](#A_2_5_ContentCheck),
[Event log compund](#Eventlogcompund),
[Event log entry](#Eventlogentry),
[Fire revision examination](#Firerevisionexamination),
[Import application into a public administration software](#Importapplicationintoapublicadministrationsoftware),
[Internal discussion](#Internaldiscussion),
[Internal referral department participation](#Internalreferraldepartmentparticipation),
[Involvement of review Board](#InvolvementofreviewBoard),
[Issuance of completion certificate (occupancy permit)](#Issuanceofcompletioncertificate(occupancypermit)),
[Issue notification letter for construction start](#Issuenotificationletterforconstructionstart),
[Issuing notification letter ](#Issuingnotificationletter),
[Mechanical plan examination](#Mechanicalplanexamination),
[Meeting with supervisor](#Meetingwithsupervisor),
[Neighbour participation](#Neighbourparticipation),
[Obtain approval of the construction conformity](#Obtainapprovaloftheconstructionconformity),
[Obtain site validity certificates](#Obtainsitevaliditycertificates),
[Participation by applicant - collect & Assess statements](#Participationbyapplicant-collectAssessstatements),
[Participation of other agencies](#Participationofotheragencies),
[Participation of public](#Participationofpublic),
[Planning / zoning review](#Planning/zoningreview),
[Post phase](#Postphase),
[Pre Consultation](#PreConsultation),
[Pre Phase](#PrePhase),
[Prepare technical report](#Preparetechnicalreport),
[Private agencies participation](#Privateagenciesparticipation),
[Property condition check](#Propertyconditioncheck),
[Public agencies participation](#Publicagenciesparticipation),
[Public inquiry](#Publicinquiry),
[Receive submission](#Receivesubmission),
[Recommendation to statutory planning committee (SPC)](#Recommendationtostatutoryplanningcommittee(SPC)),
[Registration of application](#Registrationofapplication),
[Request further documents (if needed)](#Requestfurtherdocuments(ifneeded)),
[Review phase](#Reviewphase),
[Review planning policies (by town planning committee)](#Reviewplanningpolicies(bytownplanningcommittee)),
[Security commission](#Securitycommission),
[Site Inspection](#SiteInspection),
[Submission of documents](#Submissionofdocuments),
[Submit construction conformity certificate](#Submitconstructionconformitycertificate),
[Unclassified event log entry](#Unclassifiedeventlogentry),
[Zoning review process by applicant](#Zoningreviewprocessbyapplicant),
### Obtain site validity certificates
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_1_1_1_ObtainSiteValidityCertificates`
Super-classes |[prom-bpr:A_1_1_PreConsultation](PreConsultation) (c)<br />
### Participation by applicant - collect & Assess statements
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_1_1_2_ParticipationByApplicant`
Super-classes |[prom-bpr:A_1_1_PreConsultation](PreConsultation) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_1_1_1_ObtainSiteValidityCertificates](Obtainsitevaliditycertificates) (c)<br />
### Compile application request requirement list
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_1_1_3_CompileApplicationRequestRequirementList`
Super-classes |[prom-bpr:A_1_1_PreConsultation](PreConsultation) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_1_1_2_ParticipationByApplicant](Participationbyapplicant-collectAssessstatements) (c)<br />
### Zoning review process by applicant
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_1_1_4_ZoningReviewApplicant`
Super-classes |[prom-bpr:A_1_1_PreConsultation](PreConsultation) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_1_1_3_CompileApplicationRequestRequirementList](Compileapplicationrequestrequirementlist) (c)<br />
### Pre Consultation
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_1_1_PreConsultation`
Description | <p>Giving advice by the building control authority before an application is submitted</p>
Super-classes |[prom-bpr:A_1_PrePhase](PrePhase) (c)<br />
Sub-classes |[prom-bpr:A_1_1_1_ObtainSiteValidityCertificates](Obtainsitevaliditycertificates) (c)<br />[prom-bpr:A_1_1_4_ZoningReviewApplicant](Zoningreviewprocessbyapplicant) (c)<br />[prom-bpr:A_1_1_3_CompileApplicationRequestRequirementList](Compileapplicationrequestrequirementlist) (c)<br />[prom-bpr:A_1_1_2_ParticipationByApplicant](Participationbyapplicant-collectAssessstatements) (c)<br />
### Submission of documents
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_1_2_SubmissionOfDocuments`
Super-classes |[prom-bpr:A_1_PrePhase](PrePhase) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_1_1_PreConsultation](PreConsultation) (c)<br />
### Pre Phase
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_1_PrePhase`
Super-classes |[https://w3id.org/ontobpr#Activity](https://w3id.org/ontobpr#Activity) (c)<br />
Sub-classes |[prom-bpr:A_1_1_PreConsultation](PreConsultation) (c)<br />[prom-bpr:A_1_2_SubmissionOfDocuments](Submissionofdocuments) (c)<br />
### Receive submission
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_1_1_ReceiveSubmission`
Description | <p>The submission of a building application where different conditions and requirements needs to be considered.</p>
Super-classes |[prom-bpr:A_2_1_AdministrativeCheck](Administrativecheck) (c)<br />
### Registration of application
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_1_2_RegistrationOfApplication`
Super-classes |[prom-bpr:A_2_1_AdministrativeCheck](Administrativecheck) (c)<br />
### Check/ request payment of taxes and fees
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_1_3_CheckPayment`
Super-classes |[prom-bpr:A_2_1_AdministrativeCheck](Administrativecheck) (c)<br />
### Import application into a public administration software
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_1_4_ImportApplication`
Super-classes |[prom-bpr:A_2_1_AdministrativeCheck](Administrativecheck) (c)<br />
### Completeness check
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_1_5_CompletenessCheck`
Super-classes |[prom-bpr:A_2_1_AdministrativeCheck](Administrativecheck) (c)<br />
### Administrative check
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_1_AdministrativeCheck`
Description | <p>An administrative process comprising confirmation of receipt, registration, and checking of the completeness of the submission.</p>
Super-classes |[prom-bpr:A_2_ReviewPhase](Reviewphase) (c)<br />
Sub-classes |[prom-bpr:A_2_1_1_ReceiveSubmission](Receivesubmission) (c)<br />[prom-bpr:A_2_1_4_ImportApplication](Importapplicationintoapublicadministrationsoftware) (c)<br />[prom-bpr:A_2_1_3_CheckPayment](Check/requestpaymentoftaxesandfees) (c)<br />[prom-bpr:A_2_1_2_RegistrationOfApplication](Registrationofapplication) (c)<br />[prom-bpr:A_2_1_5_CompletenessCheck](Completenesscheck) (c)<br />
### Assignment (to plan checker)
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_2_Assignment`
Description | <p>Passing on an operation or content review.</p>
Super-classes |[prom-bpr:A_2_ReviewPhase](Reviewphase) (c)<br />
### Public agencies participation
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_3_1_PublicAgencies`
Super-classes |[prom-bpr:A_2_3_ParticipationOfOtherAgencies](Participationofotheragencies) (c)<br />
### Private agencies participation
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_3_2_PrivateAgencies`
Super-classes |[prom-bpr:A_2_3_ParticipationOfOtherAgencies](Participationofotheragencies) (c)<br />
### Internal referral department participation
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_3_3_InternalReferral`
Super-classes |[prom-bpr:A_2_3_ParticipationOfOtherAgencies](Participationofotheragencies) (c)<br />
### Involvement of review Board
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_3_4_InvolvementOfReviewBoard`
Super-classes |[prom-bpr:A_2_3_ParticipationOfOtherAgencies](Participationofotheragencies) (c)<br />
### Participation of other agencies
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_3_ParticipationOfOtherAgencies`
Description | <p>Participation of other involved agencies, local authorities and any specialist authorities (for ancillary construction law), utility companies, and other experts</p>
Super-classes |[prom-bpr:A_2_ReviewPhase](Reviewphase) (c)<br />
Sub-classes |[prom-bpr:A_2_3_4_InvolvementOfReviewBoard](InvolvementofreviewBoard) (c)<br />[prom-bpr:A_2_3_3_InternalReferral](Internalreferraldepartmentparticipation) (c)<br />[prom-bpr:A_2_3_1_PublicAgencies](Publicagenciesparticipation) (c)<br />[prom-bpr:A_2_3_2_PrivateAgencies](Privateagenciesparticipation) (c)<br />
### Neighbour participation
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_4_1_NeighbourParticipation`
Super-classes |[prom-bpr:A_2_4_ParticipationOfPublic](Participationofpublic) (c)<br />
### Public inquiry
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_4_2_PublicInquiry`
Super-classes |[prom-bpr:A_2_4_ParticipationOfPublic](Participationofpublic) (c)<br />
### Participation of public
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_4_ParticipationOfPublic`
Description | <p>Participation of interested or concerned people that is essential for promoting transparency, inclusivity, and informed decision-making</p>
Super-classes |[prom-bpr:A_2_ReviewPhase](Reviewphase) (c)<br />
Sub-classes |[prom-bpr:A_2_4_2_PublicInquiry](Publicinquiry) (c)<br />[prom-bpr:A_2_4_1_NeighbourParticipation](Neighbourparticipation) (c)<br />
### Internal discussion
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_10_InternalDiscussion`
Super-classes |[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_5_9_PropertyConditionCheck](Propertyconditioncheck) (c)<br />
### Consultation with applicant
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_11_ConsultationWithApplicant`
Super-classes |[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_5_10_InternalDiscussion](Internaldiscussion) (c)<br />
### Meeting with supervisor
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_12_MeetingWithSupervisor`
Super-classes |[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_5_11_ConsultationWithApplicant](Consultationwithapplicant) (c)<br />
### Security commission
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_13_SecurityCommission`
Super-classes |[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_5_12_MeetingWithSupervisor](Meetingwithsupervisor) (c)<br />
### Recommendation to statutory planning committee (SPC)
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_14_RecommendationToStatutoryPlanningCommittee`
Super-classes |[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_5_13_SecurityCommission](Securitycommission) (c)<br />
### Review planning policies (by town planning committee)
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_15_ReviewPlanningPoliciesByTownPlanningCommittee`
Super-classes |[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_5_14_RecommendationToStatutoryPlanningCommittee](Recommendationtostatutoryplanningcommittee(SPC)) (c)<br />
### Content check
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_1_ContentCheck`
Description | <p>The examination of the submission against substantive planning and building law</p>
Super-classes |[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />
### Building committee meeting
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_2_BuildingCommitteeMeeting`
Super-classes |[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_5_1_ContentCheck](Contentcheck) (c)<br />
### Planning / zoning review
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_3_PlanningZoningReview`
Super-classes |[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_5_2_BuildingCommitteeMeeting](Buildingcommitteemeeting) (c)<br />
### Building / technical review
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_4_BuildingTechnicalReview`
Super-classes |[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_5_3_PlanningZoningReview](Planning/zoningreview) (c)<br />
### Construction law review
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_5_ConstructionLawReview`
Super-classes |[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_5_4_BuildingTechnicalReview](Building/technicalreview) (c)<br />
### Mechanical plan examination
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_6_MechanicalPlanExamination`
Super-classes |[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_5_5_ConstructionLawReview](Constructionlawreview) (c)<br />
### Fire revision examination
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_7_FireRevisionExamination`
Super-classes |[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_5_6_MechanicalPlanExamination](Mechanicalplanexamination) (c)<br />
### Prepare technical report
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_8_PrepareTechnicalReport`
Super-classes |[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_5_7_FireRevisionExamination](Firerevisionexamination) (c)<br />
### Property condition check
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_9_PropertyConditionCheck`
Super-classes |[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_5_8_PrepareTechnicalReport](Preparetechnicalreport) (c)<br />
### Content check
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_5_ContentCheck`
Description | <p>The examination of the submission against substantive planning and building law</p>
Super-classes |[prom-bpr:A_2_ReviewPhase](Reviewphase) (c)<br />
Sub-classes |[prom-bpr:A_2_5_11_ConsultationWithApplicant](Consultationwithapplicant) (c)<br />[prom-bpr:A_2_5_12_MeetingWithSupervisor](Meetingwithsupervisor) (c)<br />[prom-bpr:A_2_5_4_BuildingTechnicalReview](Building/technicalreview) (c)<br />[prom-bpr:A_2_5_9_PropertyConditionCheck](Propertyconditioncheck) (c)<br />[prom-bpr:A_2_5_14_RecommendationToStatutoryPlanningCommittee](Recommendationtostatutoryplanningcommittee(SPC)) (c)<br />[prom-bpr:A_2_5_15_ReviewPlanningPoliciesByTownPlanningCommittee](Reviewplanningpolicies(bytownplanningcommittee)) (c)<br />[prom-bpr:A_2_5_7_FireRevisionExamination](Firerevisionexamination) (c)<br />[prom-bpr:A_2_5_1_ContentCheck](Contentcheck) (c)<br />[prom-bpr:A_2_5_6_MechanicalPlanExamination](Mechanicalplanexamination) (c)<br />[prom-bpr:A_2_5_3_PlanningZoningReview](Planning/zoningreview) (c)<br />[prom-bpr:A_2_5_5_ConstructionLawReview](Constructionlawreview) (c)<br />[prom-bpr:A_2_5_2_BuildingCommitteeMeeting](Buildingcommitteemeeting) (c)<br />[prom-bpr:A_2_5_13_SecurityCommission](Securitycommission) (c)<br />[prom-bpr:A_2_5_8_PrepareTechnicalReport](Preparetechnicalreport) (c)<br />[prom-bpr:A_2_5_10_InternalDiscussion](Internaldiscussion) (c)<br />
### Completing documentation
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_6_1_CompletingDocumentation`
Super-classes |[prom-bpr:A_2_6_IssuingNotificationLetter](Issuingnotificationletter) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_6_IssuingNotificationLetter](Issuingnotificationletter) (c)<br />
### Request further documents (if needed)
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_6_2_RequestFurtherDocumentsIfNeeded`
Super-classes |[prom-bpr:A_2_6_IssuingNotificationLetter](Issuingnotificationletter) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_6_1_CompletingDocumentation](Completingdocumentation) (c)<br />
### Check stamps, payment
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_6_3_CheckStampsPayment`
Super-classes |[prom-bpr:A_2_6_IssuingNotificationLetter](Issuingnotificationletter) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_6_2_RequestFurtherDocumentsIfNeeded](Requestfurtherdocuments(ifneeded)) (c)<br />
### Check participation statements
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_6_4_CheckParticipationStatements`
Super-classes |[prom-bpr:A_2_6_IssuingNotificationLetter](Issuingnotificationletter) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_6_3_CheckStampsPayment](Checkstamps,payment) (c)<br />
### Applicant presents building application
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_6_5_ApplicantPresentsBuildingApplication`
Super-classes |[prom-bpr:A_2_6_IssuingNotificationLetter](Issuingnotificationletter) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_6_4_CheckParticipationStatements](Checkparticipationstatements) (c)<br />
### Issue notification letter for construction start
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_6_6_IssueNotificationLetterForConstructionStart`
Super-classes |[prom-bpr:A_2_6_IssuingNotificationLetter](Issuingnotificationletter) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_2_6_5_ApplicantPresentsBuildingApplication](Applicantpresentsbuildingapplication) (c)<br />
### Issuing notification letter 
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_6_IssuingNotificationLetter`
Description | <p>The issuance of the decision as to whether a project is eligible for a building permit or license to occupy and any possible enforcement action.</p>
Super-classes |[prom-bpr:A_2_ReviewPhase](Reviewphase) (c)<br />
Sub-classes |[prom-bpr:A_2_6_1_CompletingDocumentation](Completingdocumentation) (c)<br />[prom-bpr:A_2_6_5_ApplicantPresentsBuildingApplication](Applicantpresentsbuildingapplication) (c)<br />[prom-bpr:A_2_6_4_CheckParticipationStatements](Checkparticipationstatements) (c)<br />[prom-bpr:A_2_6_3_CheckStampsPayment](Checkstamps,payment) (c)<br />[prom-bpr:A_2_6_2_RequestFurtherDocumentsIfNeeded](Requestfurtherdocuments(ifneeded)) (c)<br />[prom-bpr:A_2_6_6_IssueNotificationLetterForConstructionStart](Issuenotificationletterforconstructionstart) (c)<br />
### Review phase
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_2_ReviewPhase`
Super-classes |[https://w3id.org/ontobpr#Activity](https://w3id.org/ontobpr#Activity) (c)<br />
Restrictions |[https://w3id.org/ontobpr#afterActivity](https://w3id.org/ontobpr#afterActivity) (op) **exactly** 1 [prom-bpr:A_1_PrePhase](PrePhase) (c)<br />
Sub-classes |[prom-bpr:A_2_3_ParticipationOfOtherAgencies](Participationofotheragencies) (c)<br />[prom-bpr:A_2_1_AdministrativeCheck](Administrativecheck) (c)<br />[prom-bpr:A_2_5_ContentCheck](A_2_5_ContentCheck) (c)<br />[prom-bpr:A_2_4_ParticipationOfPublic](Participationofpublic) (c)<br />[prom-bpr:A_2_2_Assignment](Assignment(toplanchecker)) (c)<br />[prom-bpr:A_2_6_IssuingNotificationLetter](Issuingnotificationletter) (c)<br />
### Obtain approval of the construction conformity
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_3_1_1_ApprovalConstructionConformity`
Super-classes |[prom-bpr:A_3_1_SiteInspection](SiteInspection) (c)<br />
### Construction completion (notification)
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_3_1_2_ConstructionCompletion`
Super-classes |[prom-bpr:A_3_1_SiteInspection](SiteInspection) (c)<br />
### Submit construction conformity certificate
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_3_1_3_ConformityCertificate`
Super-classes |[prom-bpr:A_3_1_SiteInspection](SiteInspection) (c)<br />
### Issuance of completion certificate (occupancy permit)
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_3_1_4_CompletionCertificate`
Super-classes |[prom-bpr:A_3_1_SiteInspection](SiteInspection) (c)<br />
### Site Inspection
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_3_1_SiteInspection`
Super-classes |[prom-bpr:A_3_PostPhase](Postphase) (c)<br />
Sub-classes |[prom-bpr:A_3_1_4_CompletionCertificate](Issuanceofcompletioncertificate(occupancypermit)) (c)<br />[prom-bpr:A_3_1_1_ApprovalConstructionConformity](Obtainapprovaloftheconstructionconformity) (c)<br />[prom-bpr:A_3_1_3_ConformityCertificate](Submitconstructionconformitycertificate) (c)<br />[prom-bpr:A_3_1_2_ConstructionCompletion](Constructioncompletion(notification)) (c)<br />
### Archiving
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_3_2_Archiving`
Super-classes |[prom-bpr:A_3_PostPhase](Postphase) (c)<br />
### Post phase
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#A_3_PostPhase`
Super-classes |[https://w3id.org/ontobpr#Activity](https://w3id.org/ontobpr#Activity) (c)<br />
Sub-classes |[prom-bpr:A_3_1_SiteInspection](SiteInspection) (c)<br />[prom-bpr:A_3_2_Archiving](Archiving) (c)<br />
### Event log compund
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#EventLogCompound`
Super-classes |[https://w3id.org/ontobpr#Activity](https://w3id.org/ontobpr#Activity) (c)<br />
Restrictions |[prom-bpr:hasEventLogEntry](haseventlogentry) (op) **some** [prom-bpr:EventLogEntry](Eventlogentry) (c)<br />
In domain of |[prom-bpr:hasEventLogEntry](haseventlogentry) (op)<br />
### Event log entry
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#EventLogEntry`
Super-classes |[prov:Activity](http://www.w3.org/ns/prov#Activity) (c)<br />
Sub-classes |[prom-bpr:UnclassifiedEventLogEntry](Unclassifiedeventlogentry) (c)<br />
In range of |[prom-bpr:hasEventLogEntry](haseventlogentry) (op)<br />
### Unclassified event log entry
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#UnclassifiedEventLogEntry`
Super-classes |[prom-bpr:EventLogEntry](Eventlogentry) (c)<br />

## Object Properties
[afterActivity](#afterActivity),
[has event log entry](#haseventlogentry),
[](afterActivity)
### afterActivity
Property | Value
--- | ---
IRI | `https://w3id.org/ontobpr#afterActivity`
[](haseventlogentry)
### has event log entry
Property | Value
--- | ---
IRI | `https://w3id.org/prom-bpr#hasEventLogEntry`
Super-properties |[owl:topObjectProperty](http://www.w3.org/2002/07/owl#topObjectProperty)<br />
Domain(s) |[prom-bpr:EventLogCompound](Eventlogcompund) (c)<br />
Range(s) |[prom-bpr:EventLogEntry](Eventlogentry) (c)<br />

## Named Individuals
## Namespaces
* **default (:)**
  * `https://w3id.org/prom-bpr#`
* **ct**
  * `https://standards.iso.org/iso/21597/-1/ed-1/en/Container#`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dcterms**
  * `http://purl.org/dc/terms/`
* **isoprops**
  * `https://w3id.org/isoprops#`
* **obpa**
  * `https://w3id.org/obpa#`
* **ontobpr**
  * `https://w3id.org/ontobpr`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **prom-bpr**
  * `https://w3id.org/prom-bpr#`
* **prom-bpr-instances**
  * `https://w3id.org/prom-bpr-instances#`
* **prov**
  * `http://www.w3.org/ns/prov#`
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **sdo**
  * `https://schema.org/`
* **sh**
  * `http://www.w3.org/ns/shacl#`
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **vann**
  * `http://purl.org/vocab/vann/`
* **xml**
  * `http://www.w3.org/XML/1998/namespace`
* **xsd**
  * `http://www.w3.org/2001/XMLSchema#`

## Legend
* Classes: c
* Object Properties: op
* Functional Properties: fp
* Data Properties: dp
* Annotation Properties: dp
* Properties: p
* Named Individuals: ni