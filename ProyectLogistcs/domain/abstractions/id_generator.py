class IDGenerator:

    @staticmethod
    def generate_id(repository, prefix: str):

        last_entity = repository.get_last_package()  # Fetch the last entity
        if last_entity:
            last_number = int(last_entity.id[len(prefix):])  # Extract the numeric part
        else:
            last_number = 0  # Start from 0 if no entities exist

        new_number = last_number + 1
        return f"{prefix}{new_number:03}"  # Format as PrefixXXX
