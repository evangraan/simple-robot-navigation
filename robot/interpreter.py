from . import aspects


class Interpreter:
    logger = None
    debug = False
    nav = None

    def process_instructions_file(self, instructions_file: str) -> bool:
        instructions = self.__load_instructions_file(instructions_file)
        if not instructions:
            self.logger.error("no instructions in instruction file")
            return False

        if self.__validated_instructions(instructions):
            self.nav.calculate_distance()
            self.logger.info("{:.3f} units".format(self.nav.distance))

            if self.debug:
                self.logger.debug("I am facing: " + self.nav.direction)

        return True

    def __validated_instructions(self, instructions: str) -> bool:
        invalid = self.__process_instructions(instructions)

        if invalid == len(instructions):
            self.logger.error("no valid instructions in instruction file")
            return False

        if invalid > 0:
            self.logger.warning("Warning: some instructions were invalid")

        return True

    def __load_instructions_file(self, instructions_file) -> [str]:
        if self.debug:
            print("Instruction file: " + instructions_file)
        file = open(instructions_file)
        instructions = [aspects.sanitize(instruction) for instruction in file.readlines() if
                        aspects.sanitize(instruction.strip())]
        file.close()

        return instructions

    def __process_instructions(self, instructions: str) -> int:
        invalid = 0
        for instruction in instructions:
            if self.debug:
                self.logger.debug("Executing " + instruction)

            if not self.__process_instruction(instruction):
                invalid += 1

        return invalid

    def __process_instruction(self, instruction: str) -> bool:
        if instruction not in ['L', 'R', 'F']:
            return False
        else:
            self.nav.navigate(instruction)
            if self.debug:
                self.logger.debug(self.nav.report())
        return True
