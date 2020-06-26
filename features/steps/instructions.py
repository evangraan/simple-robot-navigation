from behave import *
from robot.robot import Robot


# setup

@given(u'a robot')
def step_impl(context):
    context.robot = Robot()


@given(u'no instruction file')
def step_impl(context):
    context.instruction_file = None


@given(u'an instruction file that does not exist or cannot be opened')
def step_impl(context):
    context.instruction_file = 'features/data/thisfiledoesnotexist.instructions'


@given(u'an empty instruction file')
def step_impl(context):
    context.instruction_file = 'features/data/empty.instructions'


@given(u'a valid instruction file')
def step_impl(context):
    context.instruction_file = 'features/data/valid.instructions'


@given(u'an instruction file containing some valid and some unknown instructions')
def step_impl(context):
    context.instruction_file = 'features/data/invalid.instructions'


@given(u'an instruction file with only unknown instructions')
def step_impl(context):
    context.instruction_file = 'features/data/invalidonly.instructions'


# operation

@when(u'the robot is instructed to operate')
def step_impl(context):
    context.result = context.robot.operate(context.instruction_file, debug=True)


# assertion

@then(u'the robot notifies \'missing instructions file\'')
def step_impl(context):
    assert 'missing instructions file' in context.robot.get_notifications()


@then(u'the robot notifies \'could not open instructions file\'')
def step_impl(context):
    assert 'could not open instructions file' in context.robot.get_notifications()


@then(u'the robot notifies \'no instructions in instruction file\'')
def step_impl(context):
    assert 'no instructions in instruction file' in context.robot.get_notifications()


@then(u'the robot performs the instructions')
def step_impl(context):
    assert 'Operations: completed' in context.robot.get_notifications()


@then(u'the robot notifies the distance traveled')
def step_impl(context):
    assert any('2.236 units' in notification for notification in context.robot.get_notifications())


@then(u'the robot notifies the distance traveled using valid steps')
def step_impl(context):
    assert any('2.000 units' in notification for notification in context.robot.get_notifications())


@then(u'the robot notifies whether a circle was completed')
def step_impl(context):
    assert (context.result in [False, True])


@then(u'the robot performs the instructions that it understands')
def step_impl(context):
    assert 'Operations: completed' in context.robot.get_notifications()


@then(u'the robot ignores the instructions it does not understand')
def step_impl(context):
    assert 'Operations: completed' in context.robot.get_notifications()


@then(u'the robot notifies \'Warning: some instructions were invalid\'')
def step_impl(context):
    assert 'Warning: some instructions were invalid' in context.robot.get_notifications()


@then(u'the robot notifies \'no valid instructions in instruction file\'')
def step_impl(context):
    assert 'no valid instructions in instruction file' in context.robot.get_notifications()
