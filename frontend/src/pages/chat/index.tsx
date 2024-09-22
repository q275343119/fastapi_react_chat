import { Button, Flex } from "antd";
import { userStore } from "../../stores/user";
import { router } from "../../router";

export function Chat() {
  return (
    <div>
      聊天UI
      <div>
        <Flex gap="small" wrap>
          <Button
            type="primary"
            onClick={async () => {
              await userStore.logout();
              router.navigate("/");
            }}
          >
            登出
          </Button>
        </Flex>
      </div>
    </div>
  );
}
