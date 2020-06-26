from behave import *
from robot.robot import Robot


# assertion

@then(u'the robot notifies \'{distance}\' units')
def step_impl(context, distance):
    assert any(distance in notification for notification in context.robot.get_notifications())


@then(u'the robot returns {circle}')
def step_impl(context, circle):
    assert (str(context.result) == circle)
