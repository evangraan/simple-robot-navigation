from behave import *
from robot.robot import Robot
import time


# setup

@given(u'a valid {instruction} file')
def step_impl(context, instruction):
    context.instruction_file = instruction

# operation

@when(u'the robot is instructed to move \'F\'')
def step_impl(context):
    context.result = context.robot.operate(context.instruction_file, debug=True)


@when(u'the robot is instructed to move \'L\'')
def step_impl(context):
    context.result = context.robot.operate(context.instruction_file, debug=True)


@when(u'the robot is instructed to move \'R\'')
def step_impl(context):
    context.result = context.robot.operate(context.instruction_file, debug=True)


@when(u'the robot has executed all valid instructions')
def step_impl(context):
    pass


# assertion

@then(u'the robot notifies {moves} along its current direction')
def step_impl(context, moves):
    assert any(moves in notification for notification in context.robot.get_notifications() )


@then(u'the robot does not change {direction}')
def step_impl(context, direction):
    assert any('I am facing: ' + direction in notification for notification in context.robot.get_notifications())


@then(u'the robot does not move {position}')
def step_impl(context, position):
    assert any(position in notification for notification in context.robot.get_notifications())


@then(u'the robot changes {direction} by 90 degrees accordingly')
def step_impl(context, direction):
    assert any('I am facing: ' + direction in notification for notification in context.robot.get_notifications())


@then(u'the robot does not move')
def step_impl(context):
    before = context.robot.nav.distance
    time.sleep(0.5)
    after = context.robot.nav.distance
    assert (int(before * 10000) == int(after * 10000))  # comparing floats


@then(u'the robot does not turn')
def step_impl(context):
    before = context.robot.nav.direction
    time.sleep(0.5)
    after = context.robot.nav.direction
    assert (before == after)
