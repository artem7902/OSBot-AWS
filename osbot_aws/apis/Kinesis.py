from osbot_aws.apis.Session import Session
from osbot_aws.helpers.Method_Wrappers import cache


class Kinesis:

    @cache
    def kinesis(self):
        return Session().client('kinesis')

    def streams(self):
        return self.kinesis().list_streams()
