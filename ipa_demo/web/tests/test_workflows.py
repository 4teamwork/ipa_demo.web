from ipa_demo.web.testing import DEMO_FUNCTIONAL
from ftw.lawgiver.tests.base import WorkflowTest


class TestSESWebWorkflowSpecification(WorkflowTest):
    layer = DEMO_FUNCTIONAL
    workflow_path = '../profiles/default/workflows/ipa_demo_web_workflow'
