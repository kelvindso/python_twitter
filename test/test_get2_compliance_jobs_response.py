# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints  # noqa: E501

    The version of the OpenAPI document: 2.49
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import twitter
from twitter.models.get2_compliance_jobs_response import Get2ComplianceJobsResponse  # noqa: E501
from twitter.rest import ApiException

class TestGet2ComplianceJobsResponse(unittest.TestCase):
    """Get2ComplianceJobsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Get2ComplianceJobsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = twitter.models.get2_compliance_jobs_response.Get2ComplianceJobsResponse()  # noqa: E501
        if include_optional :
            return Get2ComplianceJobsResponse(
                data = [
                    twitter.models.compliance_job.ComplianceJob(
                        created_at = '2021-01-06T18:40:40Z', 
                        download_expires_at = '2021-01-06T18:40:40Z', 
                        download_url = '', 
                        id = '1372966999991541762', 
                        name = 'my-job', 
                        status = 'created', 
                        type = 'tweets', 
                        upload_expires_at = '2021-01-06T18:40:40Z', 
                        upload_url = '', )
                    ], 
                errors = [
                    twitter.models.problem.Problem(
                        detail = '', 
                        status = 56, 
                        title = '', 
                        type = '', )
                    ], 
                meta = twitter.models.get2_compliance_jobs_response_meta.Get2ComplianceJobsResponse_meta(
                    result_count = 56, )
            )
        else :
            return Get2ComplianceJobsResponse(
        )

    def testGet2ComplianceJobsResponse(self):
        """Test Get2ComplianceJobsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
