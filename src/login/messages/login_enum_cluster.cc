#include "login/messages/login_enum_cluster.h"

#include "login/login_client.h"

using namespace login;
using namespace messages;
using namespace std;

LoginEnumCluster login::messages::BuildLoginEnumCluster(shared_ptr<LoginClient> login_client, const vector<GalaxyStatus>& galaxy_status) {
    LoginEnumCluster message;
    message.max_account_chars = 2;

    std::for_each(galaxy_status.begin(), galaxy_status.end(), [&message] (const GalaxyStatus& status) {            
        Cluster cluster;
        cluster.distance = status.distance;
        cluster.server_id = status.galaxy_id;
        cluster.server_name = status.name;

        message.servers.push_back(cluster);
    });

    return message;
}